farm_loop(setup_diverse)

def setup_diverse():
    size = get_world_size()
    mid = (size - 1) // 2
    
    # a pumpkin corner
    if get_pos_x() <= mid and get_pos_y() <= mid:
        ensure_entity(Entities.Pumpkin)
    # carrots in the top-left corner (for now)
    elif get_pos_x() < mid:
        ensure_entity(Entities.Carrots)
    # sunflowers
    elif get_pos_y() <= mid:
        ensure_entity(Entities.Sunflower)
    # corner cacti
    elif get_pos_x() >= size - 2 and get_pos_y() >= size - 2:
        ensure_entity(Entities.Cactus)
    # a tree "chessboard" in the rest
    elif get_pos_x() % 2 == get_pos_y() % 2:
        ensure_entity(Entities.Tree)
    else:
        ensure_entity(Entities.Grass)
        