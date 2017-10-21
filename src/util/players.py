import string
import math
import unicodedata

from datetime import date
# from database.connection import DATABASE_NAME, connection

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
        player = connection.NBAI.players.find_one({'player_id' : int(playerid)}, {'player_id' : 1, 'player_name' : 1, 'height' : 1, 'weight' : 1, 'dob' : 1, 'position' : 1, 'jersey' : 1, 'last_year' : 1, '_id' : 0})
    except:
        print("ABFDF")
        return None

    if not player or player['last_year'] != date.today().year :
        return None
    player['position'] = get_player_position(player['position'])
    player['height']   = get_player_height(player['height'])
    player['age']      = get_player_age(player['dob'])

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
