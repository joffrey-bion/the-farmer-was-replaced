def always_true():
	return True
	
def farm_loop(
	setup_current_tile,
	loop_condition = always_true,
	min_water_threshold = 0.3,
	buy_tanks_if_needed = False
):
    sunflower_petal_counts = {}
    grid_size = get_world_size()
    fertilizer_unlocked = num_unlocked(Unlocks.Fertilizer) > 0
    
    while loop_condition():
        harvest_if_possible(sunflower_petal_counts, fertilizer_unlocked)
        setup_current_tile()      
        
        if get_entity_type() == Entities.Sunflower:
            sunflower_petal_counts[get_pos()] = measure()
        
        if get_entity_type() == Entities.Cactus:
            swap_cactus_if_needed()
        
        if not can_harvest(): # save water if the plant is already grown
            ensure_min_water(min_water_threshold, buy_tanks_if_needed)              
        
        move_to_next_tile(grid_size)

def harvest_if_possible(sunflower_petal_counts, fertilizer_unlocked):
    entity_type = get_entity_type()
    if fertilizer_unlocked and not can_harvest() and entity_type != None:
        fertilize()
    if not can_harvest(): # we STILL can't
        return
    if entity_type == Entities.Sunflower:
        harvest_sunflower_if_biggest(sunflower_petal_counts)
    elif entity_type == Entities.Cactus:
        harvest_cactus_if_sorted()
    else:
        harvest()
    
def harvest_sunflower_if_biggest(sunflower_petal_counts):
    if measure() == max_value(sunflower_petal_counts):
        harvest()
        pos = get_pos()
        if pos in sunflower_petal_counts:
            sunflower_petal_counts.pop(pos)                 

def harvest_cactus_if_sorted():
    index_max = get_world_size() - 1
    size = measure()
    west = measure(West)
    east = measure(East)
    south = measure(South)
    north = measure(North)
    if ((get_pos_x() == 0         or (west  != None and size >= west))
    and (get_pos_x() == index_max or (east  != None and size <= east))
    and (get_pos_y() == 0         or (south != None and size >= south))
    and (get_pos_y() == index_max or (north != None and size <= north))):
        harvest()

def swap_cactus_if_needed():
    size = measure()
    west = measure(West)
    east = measure(East)
    south = measure(South)
    north = measure(North)
    if west != None and size < west:
        swap(West)
        return
    if east != None and size > east:
        swap(East)
        return
    if south != None and size < south:
        swap(South)
        return
    if north != None and size > north:
        swap(North)
        return
        
def move_to_next_tile(grid_size):
    if get_pos_y() == grid_size - 1:
        move(East)
    move(North)
    
def get_pos():
    return get_pos_x(), get_pos_y()
    
def max_value(dictionary):
    result = 0
    for k in dictionary:
        result = max(result, dictionary[k])
    return result
    