import string
import math
import unicodedata

from datetime import date
from database.connection import DATABASE_NAME, connection
from random import randint

"""
Attemps to create a player dict containing information to be rendered.

Connects to the database and searches for a player based on a playerid passed
in from the path.  If the player cannot be located in the database or is no
longer active, we will return none and the server will return a 404 status code.

If the player is found and is active, call functions to format position and
height and to calculate age from the player dob.

Returns the player dict.
"""
def extract_player_info(playerid):
    try:
        player = connection.NBAI.players.find_one({'player_id' : int(playerid)},
         {'player_id'  : 1,
         'player_name' : 1,
         'height'      : 1,
         'weight'      : 1,
         'dob'         : 1,
         'position'    : 1,
         'jersey'      : 1,
         'last_year'   : 1,
         'team_id'     : 1,
         '_id'         : 0})
    except:
        return None

    if not player or player['last_year'] != date.today().year :
        return None
    player['team_abbr'] = get_player_team(player['team_id'])
    player['position']  = get_player_position(player['position'])
    player['height']    = get_player_height(player['height'])
    player['age']       = get_player_age(player['dob'])

    return player


"""
Given a player position from the database, formats the position for display.

If the player has a position in the database, we must first convert the string
from unicode to ascii to call translate, and we then remove all lowercase
letters so that Forward => F, Guard-Forward => G-F, etc...

Returns the position if there is one, otherwise returns an empty string.
"""
def get_player_position(position):
    if position:
        unicode_to_string  = unicodedata.normalize('NFKD', position).encode('ascii','ignore')
        return unicode_to_string.translate(None,string.ascii_lowercase)
    return ''


"""
Given a player height from the database in inches, formats it for display.

Returns height in feet and inches if the player has a height in the database,
returns an empty string otherwise.
"""
def get_player_height(height):
        return str(int(math.floor(int(height)/12))) + "'" + str(int(height)%12) + '"' if height else ''


"""
Given a player date of birth from the database, calculates the player's age.

Returns the player's age if a dob exists, returns an empty string otherwise.
"""
def get_player_age(dob):
        if(dob):
            dob_year, dob_month, dob_day = [int(x) for x in dob.split('-')]
            today = date.today()
            return today.year - dob_year - ((today.month, today.day) < (dob_month, dob_day))
        else:
            return ''

"""
Given a team id, retrieves the team abbreviation.

Returns a string - team abbreviation if found, empty string otherwise.
"""
def get_player_team(teamid):
    try:
        team_abbr = connection.NBAI.teams.find_one({'team_id' : int(teamid)}, {'team_abbr' : 1, '_id' : 0})['team_abbr']
        return team_abbr
    except:
        return ''

"""
Loads 2 players from teams playing on the current day.

Returns a list of players, position, value, opponent.
"""
def load_todays_players():
    today = date.today()
    todays_date = str(today.year) + str(today.month) + str(today.day)
    games = {}
    output = []

    todays_games = connection.NBAI.schedules.find({'game_date' : todays_date})
    for game in todays_games:
        team_abbr = connection.NBAI.teams.find_one({'team_id' : int(game['team_id'])}, {'team_abbr' : 1, '_id' : 0})['team_abbr']
        game_id = game['game_id']
        if game_id not in games:
            games[game_id] = {}
            games[game_id]['teams'] = []
        games[game_id]['teams'].append({team_abbr : None})

    for game_id, game in games.items():
        for team in game['teams']:
            team1 = game['teams'][0].keys()[0]
            team2 = game['teams'][1].keys()[0]
            opp = team1 if team.keys()[0] == team2 else team2


            team_abbr = team.items()[0][0]
            roster_ids = connection.NBAI.teams.find({'team_abbr' : team_abbr}, {'roster' : 1, '_id' : 0})[0]['roster']
            roster = []
            i = 0
            for player in roster_ids:
                player_item = extract_player_info(int(player))
                if(player_item):
                    roster.append(player_item['player_name'])
                    value = ['Overvalued', 'Undervalued']
                    if(i < 2):
                        output.append([player_item['player_name'], team_abbr, player_item['position'], opp, randint(10, 32), value[randint(0,1)]])
                else:
                    continue
                i += 1
    return output

"""
Loads todays teams playing in games from the database.

Returns a list team abbreviations.
"""
def get_todays_games():
    today = date.today()
    todays_date = str(today.year) + str(today.month) + str(today.day)
    games = []

    todays_games = connection.NBAI.schedules.find({'game_date' : todays_date})
    for game in todays_games:
        team_abbr = connection.NBAI.teams.find_one({'team_id' : int(game['team_id'])}, {'team_abbr' : 1, '_id' : 0})['team_abbr']
        games.append(team_abbr)
    return games
