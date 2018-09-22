
#sp1: þar sem föll eru nýrra fyrirbæri fyrir mér en if setningarnar fannst 
#mér það nokkuð einfalt, þó er mikil hætta á villum. 

#sp2: seinni implementation klárlega lesanlegri þar sem hann tekur í raun færri línur 
#hægt að "fela" kóðana í föllum. Einnig hjálpar að flokka niður verkefnin í smærri verkefni
#taka bara eitt "task" í hverju falli. 

#sp3: kóðarnir eru svipaðir hjá mér, veit svosem ekki alveg hvað svarið hér er. 

def location(a,b):
    if a == 1 and b == 1:
        poss_move = [NORTH]
    elif a == 1 and b == 2:
        poss_move = [EAST, NORTH, SOUTH]
    elif a == 1 and b == 3:
        poss_move = [SOUTH, EAST]
    elif a == 2 and b == 1:
        poss_move = [NORTH]
    elif a == 2 and b == 2:
        poss_move = [SOUTH, WEST]
    elif a == 2 and b == 3:
        poss_move = [EAST,WEST]
    elif a == 3 and b == 3:
        poss_move = [SOUTH,WEST]
    elif a == 3 and b == 2:
        poss_move = [NORTH,SOUTH]
    return poss_move
 
def printer (direction):
    printline = ""
    if direction == [NORTH]:
        printline = "(N)orth"
    elif direction == [EAST, NORTH, SOUTH]:
        printline = "(E)ast or (N)orth or (S)outh."
    elif direction == [SOUTH, EAST]:
        printline = "(E)ast or (S)outh."
    elif direction ==  [SOUTH, WEST]:
        printline = "(S)outh or (W)est."
    elif direction == [EAST,WEST]:
        printline = "(E)ast or (W)est."
    elif direction ==  [SOUTH,WEST]:
        printline = "(S)outh or (W)est."
    elif direction == [NORTH,SOUTH]:
        printline = "(N)orth or (S)outh."
    return printline  
   
 
x = 1
y = 1
 
NORTH = "n"
SOUTH = "s"
EAST = "e"
WEST = "w"
 
print_move = True
 
while x != 3 or y != 1:
    check = location(x,y)
    printliner = printer(check)
   
    if print_move:
        print("You can travel: {}".format(printliner))
    print_move = True
 
    move = input("Direction: ")
 
    move = move.lower()
   
    if move not in check:
        print("Not a valid direction!")
        print_move = False
        continue
   
    if move == NORTH:
        y += 1
    elif move == SOUTH:
        y -= 1
    elif move == EAST:
        x += 1
    elif move == WEST:
        x -= 1
   
 
print("Victory!")