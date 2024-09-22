def farm_hay_single_tile(desired):
	while num_items(Items.Hay) < desired:
		if can_harvest():
			harvest()

def farm_hay_3_tiles(desired):
	while num_items(Items.Hay) < desired:
		if can_harvest():
			harvest()
			move(North)
		
def farm_wood_3_tiles(desired):
	while num_items(Items.Wood) < desired:
		if can_harvest():
			harvest()
			ensure_entity(Entities.Bush)
			move(North)
		
def farm_wood_9_tiles(desired):
	while num_items(Items.Wood) < desired:
		if can_harvest():
			harvest()
			ensure_entity(Entities.Bush)
			move(North)
			
def farm_single_item(item_type, quantity, min_water_threshold = 0.3):
	entity_type = items_to_plant_entities[item_type]
	seed_type = get_required_seed_type(entity_type)
	if seed_type != None:
		cost = get_cost(seed_type)
		for type in cost:
			farm_single_item(type, cost[type] * quantity, min_water_threshold)
	
	def setup():
		ensure_entity(entity_type)
	def is_missing_items():
		return num_items(item_type) < quantity
	farm_loop(setup, is_missing_items, min_water_threshold, item_type == Items.Wood)

def farm_to_unlock(desired_unlock, min_water_threshold = 0.3):
	cost = get_cost(desired_unlock)
	for type in cost:
		farm_single_item(type, cost[type], min_water_threshold)
	unlock(desired_unlock)


def has_items(items):
	for type in items:
		desired = items[type]
		current = num_items(type)
		if current < desired:
			return False
	return True
	