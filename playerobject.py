from baseobject import BaseObject, connection

TABLE_NAME = 'players'

@connection.register
class PlayerObject(BaseObject):

    __collection__ = TABLE_NAME


    ## This class only exists to prevent typos.
    ## It's not needed, but it adds a layer of safety.
    class f():
	player_id = 'player_id'	
	name = 'name' 			#name
       	dob  = 'dob' 			#date of birth
	height = 'height'		#height	
	team = 'team'
	exp = 'exp' 			#experience years in the league
	games_dict = 'games_dict'	
		

    structure = {
	f.player_id : unicode,
	f.name : unicode,
       	f.dob : unicode,
	f.height : unicode,
	f.team : unicode,
	f.exp : unicode,
	f.games_dict : dict		#dict of games played
	
		}

    required_fields = [
	f.player_id,        
	f.name,
        f.dob,
	f.height,
	f.team,
        f.exp,
	f.games_dict,

    ]

    default_values = {
	#no default values
    }

