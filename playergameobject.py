from baseobject import BaseObject, connection

TABLE_NAME = 'player_stats'

@connection.register
class PlayerGameObject(BaseObject):

    __collection__ = TABLE_NAME


    ## This class only exists to prevent typos.
    ## It's not needed, but it adds a layer of safety.
    class f():
	player_id = 'player_id'
	game_id = 'game_id'		
	minutes = 'minutes'			#minutes
	fgm-fga = 'fgm-fga'			#field goals made - attempted
	fgp = 'fgp'				#field goal percentage
	tpm-tpa = 'tpm-tpa'			#three points made - attempted
	tpp = 'tpp'				#three point percentage
	ftm-fta = 'ftm-fta'			#free throws made - attempted
	ftp = 'ftp'				#free throws percentage
	reb = 'reb'				#rebounds
	ast = 'ast'				#assists
	blk = 'blk'				#blocks
	stl = 'stl'				#steals
	pf = 'pf'				#fouls
	to = 'to'				#turnovers
	pts = 'pts'				#points scored in game
		

    structure = {
	f.player_id : unicode,
	f.game_id : unicode,
	f.min : unicode,
	f.fgm-fga : unicode,
	f.fgp : unicode,
	f.tpm-tpa : unicode,
	f.tpp : unicode,
	f.ftm-fta : unicode,
	f.ftp : unicode,
	f.reb : unicode,
	f.ast : unicode,
	f.blk : unicode,
	f.stl : unicode,
	f.pf : unicode,
	f.to : unicode,
	f.pts : unicode
	
		}

    required_fields = [
	f.player_id,
	f.game_id,
	f.min,
	f.fgm-fga,
	f.fgp,
	f.tpm-tpa,
	f.tpp,
	f.ftm-fta,
	f.ftp,
	f.reb,
	f.ast,
	f.blk,
	f.stl,
	f.pf,
	f.to,
	f.pts

    ]

    default_values = {
	#no default values
    }

