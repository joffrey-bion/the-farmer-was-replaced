# Speed 1 = 20 hay
# Speed 2 = 10 wood
    
# Expand 1 = 30 hay
# Expand 2 = 20 wood

# Plant 1 = 50 hay
	
# Grass 1 = 100 hay
	
# Carrot 1 = 100 wood
	
# A: 4704 - 4714
# B: 17326 - 17335
# C: 38459 - 38550
# D: 53710 
	
	
#bush_9_9 = [
#    [Entities.Bush, Entities.Bush, Entities.Bush],
#    [Entities.Bush, Entities.Bush, Entities.Bush],
#    [Entities.Bush, Entities.Bush, Entities.Bush],
#]
#farm_loop_matrix(bush_9_9, {Items.Wood:100}, 0)
	
#grass_bush_carrots = [
#    [Entities.Carrots, Entities.Carrots, Entities.Carrots],
#    [Entities.Bush, Entities.Bush, Entities.Bush],
#    [Entities.Grass, Entities.Grass, Entities.Grass],
#]
#farm_loop_matrix(grass_bush_carrots, get_cost(Unlocks.Speed), 0)
	

def farm_loop_matrix(matrix, desired_items, min_water_threshold = 0.3):
	def setup():
		type = matrix[get_pos_y()][get_pos_x()]
		ensure_entity(type)
	
	def is_missing_items():
		return not has_items(desired_items)
		
	farm_loop(setup, is_missing_items, min_water_threshold)