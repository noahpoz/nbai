from baseobject import BaseObject, connection

TABLE_NAME = 'game_stats'

@connection.register
class TeamGameObject(BaseObject):

    __collection__ = TABLE_NAME


    ## This class only exists to prevent typos.
    ## It's not needed, but it adds a layer of safety.
    class f():
	game_id = 'game_id' 			
       	home_team = 'home_team'
	away_team = 'away_team'
	home_score = 'home_score'
	away_score = 'away_score'
	minutes = 'minutes'
	home_players = 'home_players'
	away_players = 'away_players'
	games_dict = 'games_dict'	
		

    structure = {
	f.game_id : unicode,
       	f.home_team : unicode,
	f.away_team : unicode,
	f.home_score : unicode,
	f.away_score : unicode,
	f.minutes : unicode,
	f.home_players : list,		#list of home team players that played in game.
	f.away_players : list,		#list of away team players that played in game.
	f.games_dict : dict		#dict of games played
	
		}

    required_fields = [
     	f.game_id,
       	f.home_team,
	f.away_team,
	f.home_score,
	f.away_score,
	f.minutes,
	f.home_players,
	f.away_players,
	f.games_dict 		#dict of games played

    ]

    default_values = {
	#no default values
    }

