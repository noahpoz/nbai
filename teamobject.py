from baseobject import BaseObject, connection

TABLE_NAME = 'teams'

@connection.register
class TeamObject(BaseObject):

    __collection__ = TABLE_NAME


    ## This class only exists to prevent typos.
    ## It's not needed, but it adds a layer of safety.
    class f():
	team_id = 'team_id'
	name = 'name' 			
	roster = 'roster'			
	games_dict = 'games_dict'	
		

    structure = {
	f.team_id : unicode,
       	f.name : unicode,
	f.roster : list,		#list of active players avg 14
	f.games_dict : dict		#dict of games played
	
	}

    required_fields = [
        f.team_id,
        f.name,
	f.roster,
	f.games_dict,

    ]

    default_values = {
	#no default values
    }

