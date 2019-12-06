# Main game file

import zork

def PrintOutput(s):
    print("OUTPUT", s)
    
loop = zork.Play_Zork()

while True:

    while loop == 4:

        print("---------------------------------------------------------")
        print("You are standing in an open field west of a white house, with a boarded front door.")
        print("You can see a small lake to the north.")
        print("(A secret path leads southwest into the forest.)")
        print("There is a Small Mailbox.")
        second = input("What do you do? ")
        room = zork.room4(second, [])
        loop = room[0]

    while loop == 1:

        print("---------------------------------------------------------")
        print("You find yourself at the edge of a beautiful lake aside rolling hills.")
        print("A small pier juts out into the lake.")
        print("A fishing rod rests on the pier.")
        print("(You can see a white house in the distance to the south.)")
        north_house_inp = input("What do you do? ")
        room = zork.room1(north_house_inp, [])
        loop = room[0]
        
    while loop == 8:

        print("---------------------------------------------------------")
        print("This is a forest, with trees in all directions. To the east, there appears to be sunlight.")
        forest_inp = input("What do you do? ")
        room = zork.room8(forest_inp, [])
        loop = room[0]

    while loop == 9:

        print("---------------------------------------------------------")
        print("You are in a clearing, with a forest surrounding you on all sides. A path leads south.")
        print("There is an open grating, descending into darkness.")
        grating_inp = input("What do you do? ")
        room = zork.room9(grating_inp, [])
        loop = room[0]

    while loop == 10:

        print("---------------------------------------------------------")
        print("You are in a tiny cave with a dark, forbidding staircase leading down.")
        print("There is a skeleton of a human male in one corner.")
        cave_inp = input("What do you do? ")
        room = zork.room10(cave_inp, [])
        loop = room[0]

    while loop == 11:

        print("---------------------------------------------------------")
        print("You have entered a mud-floored room.")
        print("Lying half buried in the mud is an old trunk, bulging with jewels.")
        last_inp = input("What do you do? ")
        room = zork.room11(last_inp, [])
        loop = room[0]

    while loop == 12:

        print("---------------------------------------------------------")
        print("You are behind the house. Paths are south or west")
        user_input12 = input("What do you do? ")
        room = zork.room12(user_input12, [])
        loop = room[0]

    while loop == 13:

        print("---------------------------------------------------------")
        print('You find yourself in a dimly lit kitchen with dust covering the floor.')
        print('A latern rests on the kitchen island')
        print('A set of stairs leads up to another room')
        user_input13 = input("What do you do? ")
        room = zork.room13(user_input13, [])
        loop = room[0]

    while loop == 14:

        print("---------------------------------------------------------")
        print('You are in the top of the house, the attic. Path is to go back down')
        user_input14 = input("What do you do? ")
        room = zork.room14(user_input14, [])
        loop = room[0]

    while loop == 15:

        print("---------------------------------------------------------")
        print('You walk up to an entrance with a sign that reads \'MAZE\'.')
        print('North leads to the cave, South enters the maze and East goes to neither.')
        user_input15 = input("What do you do? ")
        room = zork.room15(user_input15, [])
        loop = room[0]

    while loop == 16:

        print("---------------------------------------------------------")
        print('You are on the inside of the maze.')
        print('North takes you to the start of the maze.')
        print('You can go any direction.')
        user_input16 = input("What do you do? ")
        room = zork.room16(user_input16, [])
        loop = room[0]

    while loop == 17:
        
        print("---------------------------------------------------------")
        print('You are by a beautiful garden.')
        print('Stay and look at the beautiful flowers.')
        user_input17 = input("What do you do? ")
        room = zork.room17(user_input17, [])
        loop = room[0]

    
