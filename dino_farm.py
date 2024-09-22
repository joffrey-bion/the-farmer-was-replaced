# CAREFUL: consumes a lot of cacti

while True:
    if can_harvest():
        harvest()
    trade(Items.Egg)
    use_item(Items.Egg)
    move_to_next_tile()