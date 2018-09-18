x = 1
y = 1

NORTH = "n"
SOUTH = "s"
EAST = "e"
WEST = "w"

while x != 3 or y != 1:
    if x == 1 and y == 1:
        possible_move = NORTH
        output1 = "(N)orth"
    elif x == 1 and y == 2: 
        possible_move = NORTH, EAST, SOUTH
        output1= "(N)orth or (E)ast or (S)outh"
    elif x == 1 and y == 3:
        possible_move = EAST, SOUTH
        output1 = "(E)ast, (S)outh"
    elif x == 2 and y == 1:
        possible_move = NORTH
        output1 = "(N)orth"
    elif x == 2 and y == 2:
        possible_move = SOUTH, WEST
        output1 = "(S)outh or (W)est"
    elif x == 2 and y == 3: 
        possible_move = EAST, WEST
        output1 = "(E)ast or (W)est"
    elif x == 3 and y == 3:
        possible_move = WEST, SOUTH
        output1 = "(W)est, (S)outh"
    elif x == 3 and y == 2:
        possible_move = NORTH, SOUTH
        output1 = "(N)orth or (S)outh"


    print("You can travel: {}".format(output1))
    move = input("Direction: ")
    
    if move.lower() not in [NORTH,SOUTH,EAST,WEST]:
        print("Not a valid direction!")

    if move.lower() == NORTH:
        y += 1
    elif move.lower() == SOUTH:
        y -= 1
    elif move.lower() == EAST:
        x += 1
    elif move.lower() == WEST:
        x -= 1

print("Victory!")
 



