def run_maze_round():
    trigger_maze()
    solve_maze()

def trigger_maze():
    ensure_entity(Entities.Bush)
    ensure_min_water(0.9, False)

    while not can_harvest():
        do_a_flip()

    # in a maze, we'd get Hedge or Treasure
    while get_entity_type() == Entities.Bush:
        fertilize()

# follows the right wall to the treasure
def solve_maze():
    directions = [North, East, South, West]
    dir_index = 0
    
    def straight():
        return directions[dir_index]
    def right():
        return directions[(dir_index + 1) % 4]
    
    while get_entity_type() != Entities.Treasure:
        moved_right = move(right())
        if moved_right:
            # we rotated right by moving
            dir_index = (dir_index + 1) % 4
        else:
            moved_straight = move(straight())
            if not moved_straight:
                # let's rotate left and carry on
                dir_index = (dir_index - 1) % 4
    
    harvest()