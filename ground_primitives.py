def ensure_entity(entity_type):
    if get_entity_type() == entity_type:
        return
    ground_type = get_optimal_ground_type(entity_type)
    ensure_empty_ground(ground_type)
    if entity_type != Entities.Grass:
        ensure_seed_for(entity_type)
        plant(entity_type)
     
def get_optimal_ground_type(entity_type):
    if entity_type == Entities.Grass:
        return Grounds.Turf
    return Grounds.Soil 
        
# This ensures the proper ground type but also that we can plant
def ensure_empty_ground(groundType):
    if get_ground_type() != groundType:
        till() # toggles between Soil and Turf
    # destroy a potential existing entity
    harvest() 
        
def ensure_seed_for(entity_type):
    seed_type = get_required_seed_type(entity_type)
    if seed_type != None and num_items(seed_type) == 0:
        trade(seed_type)

def get_required_seed_type(entity_type):
    required_seeds = get_cost(entity_type)
    for seed_type in required_seeds:
        return seed_type # there is only one, we return asap
    return None
        
def ensure_min_water(min_fraction, buy_tanks_if_needed):
    if get_ground_type() != Grounds.Soil or get_water() >= min_fraction:
        return # no need to water in this case
        
    if num_items(Items.Water_Tank) > 0:
        use_item(Items.Water_Tank)
    elif buy_tanks_if_needed:
        # tanks didn't fill fast enough, let's buy more for next time
        trade(Items.Empty_Tank)

def fertilize():
    if num_items(Items.Fertilizer) == 0:
        trade(Items.Fertilizer)
    use_item(Items.Fertilizer)
    
    