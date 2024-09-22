# CAREFUL: consumes a lot of pumpkins (fertilizer)

for _ in range(get_world_size() * get_world_size()):
    ensure_smallest_sunflower()
    move_to_next_tile()

while True:
    if can_harvest():
        harvest()
        ensure_entity(Entities.Sunflower)
    
    ensure_min_water(1, False)
    fertilize()
        
def ensure_smallest_sunflower():
	ensure_entity(Entities.Sunflower)
    while (measure() > 7):
        harvest()
		ensure_entity(Entities.Sunflower)