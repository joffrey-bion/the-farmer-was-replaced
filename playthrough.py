items_to_plant_entities = {
	Items.Hay:Entities.Grass,
	Items.Wood:Entities.Bush,
	Items.Carrot:Entities.Carrots,
	Items.Pumpkin:Entities.Pumpkin,
	Items.Cactus:Entities.Cactus
}

timed_reset()

farm_hay_single_tile(20)
unlock(Unlocks.Speed)

farm_hay_single_tile(30)
unlock(Unlocks.Expand) # now 1x3

farm_hay_3_tiles(50)
unlock(Unlocks.Plant)

farm_wood_3_tiles(10)
unlock(Unlocks.Speed)

farm_wood_3_tiles(20)
unlock(Unlocks.Expand) # now 3x3

farm_to_unlock(Unlocks.Carrots)
farm_to_unlock(Unlocks.Speed)
farm_to_unlock(Unlocks.Grass)


while True:
	do_a_flip()