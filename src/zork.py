import items

def Play_Zork():
        loop = 4
        print("---------------------------------------------------------")
        print("Welcome to Zork - The Unofficial Python Version.")
        return loop

def exit_function(exit_inp):
        if exit_inp.lower() == 'dead':
                exit()
                
def room4(second, item_list):             

        if second.lower() == ("take mailbox"):
                print("---------------------------------------------------------")
                print("It is securely anchored.")
                loop = 4
                alive_dead = 'Alive'
        elif second.lower() == ("open mailbox"):
                print("---------------------------------------------------------")
                print("Opening the small mailbox reveals a leaflet.")
                loop = 4
                alive_dead = 'Alive'
        elif second.lower() == ("go north"):
                loop = 1
                alive_dead = 'Alive'
        elif second.lower() == ("open door"):
                print("---------------------------------------------------------")
                print("The door cannot be opened.")
                loop = 4
                alive_dead = 'Alive'
        elif second.lower() == ("take boards"):
                print("---------------------------------------------------------")
                print("The boards are securely fastened.")
                loop = 4
                alive_dead = 'Alive'
        elif second.lower() == ("look at house"):
                print("---------------------------------------------------------")
                print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
                alive_dead = 'Alive'
        elif second.lower() == ("go southwest"):
                loop = 8
                alive_dead = 'Alive'
        elif second.lower() == ("read leaflet"):
                print("---------------------------------------------------------")
                print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
                loop = 4
                alive_dead = 'Alive'
        elif second.lower() == ('go east'):
                loop = 12
                alive_dead = 'Alive'
        elif second.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                alive_dead = 'Dead'
                print("---------------------------------------------------------")
                dead_inp = alive_dead
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
        return [loop, alive_dead]

def room1(north_house_inp, item_list):
        
        if north_house_inp.lower() == ("go south"):
                loop = 4
                alive_dead = 'Alive'
        elif north_house_inp.lower() == ("swim"):
                print("---------------------------------------------------------")
                print("You don't have a change of clothes and you aren't here on vacation.")
                loop = 1
                alive_dead = 'Alive'
        elif north_house_inp.lower() == ("fish"):
                print("---------------------------------------------------------")
                print("You spend some time fishing but nothing seems to bite.")
                loop = 1
                alive_dead = 'Alive'
        elif north_house_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
        return [loop, alive_dead]
        
def room8(forest_inp, item_list):

        if forest_inp.lower() == ("go west"):
                print("---------------------------------------------------------")
                print("You would need a machete to go further west.")
                loop = 8
                alive_dead = 'Alive'
        elif forest_inp.lower() == ("go north"):
                print("---------------------------------------------------------")
                print("The forest becomes impenetrable to the North.")
                loop = 8
                alive_dead = 'Alive'
        elif forest_inp.lower() == ("go south"):
                print("---------------------------------------------------------")
                print("Storm-tossed trees block your way.")
                loop = 8
                alive_dead = 'Alive'
        elif forest_inp.lower() == ("go east"):
                loop = 9
                alive_dead = 'Alive'
        elif forest_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
        return [loop, alive_dead]

def room9(grating_inp, item_list):

        if grating_inp.lower() == ("go south"):
                print("---------------------------------------------------------")
                print("You see a large ogre and turn around.")
                loop = 9
                alive_dead = 'Alive'
        elif grating_inp.lower() == ("descend grating"):
                loop = 10
                alive_dead = 'Alive'
        elif grating_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
        return [loop, alive_dead]

def room10(cave_inp, item_list):

        if cave_inp.lower() == ("descend staircase"):
                loop = 11
                alive_dead = 'Alive'
        elif cave_inp.lower() == ("take skeleton"):
                print("---------------------------------------------------------")
                print("Why would you do that? Are you some sort of sicko?")
                loop = 10
                alive_dead = 'Alive'
        elif cave_inp.lower() == ("smash skeleton"):
                print("---------------------------------------------------------")
                print("Sick person. Have some respect mate.")
                loop = 10
                alive_dead = 'Alive'
        elif cave_inp.lower() == ("light up room"):
                print("---------------------------------------------------------")
                print("You would need a torch or lamp to do that.")
                loop = 10
                alive_dead = 'Alive'
        elif cave_inp.lower() == ("break skeleton"):
                print("---------------------------------------------------------")
                print("I have two questions: Why and With What?")
                loop = 10
                alive_dead = 'Alive'
        elif cave_inp.lower() == ("go down staircase"):
                loop = 11
                alive_dead = 'Alive'
        elif cave_inp.lower() == ("scale staircase"):
                loop = 11
                alive_dead = 'Alive'
        elif cave_inp.lower == ('go south'):
                loop = 15
                alive_dead = 'Alive'
        elif cave_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)
        elif cave_inp.lower() == ("scale staircase"):
                loop = 11
        else:
                print("---------------------------------------------------------")
        return [loop, alive_dead]

def room11(last_inp, item_list):
        if last_inp.lower() == ("open trunk"):
                print("---------------------------------------------------------")
                print("You have found the Jade Statue and have completed your quest!")
                loop = 11
                alive_dead = 'Alive'
        elif last.inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
        return [loop, alive_dead]

def room12(user_input12, item_list):
        if user_input12.lower() == ('going south'):
                loop = 4
                alive_dead = 'Alive'
        elif user_input12.lower() == ('going west'):
                print('Opening a rickety window you climb into the house')
                loop = 12
                alive_dead = 'Alive'
        elif user_input12.lower() == ('kick the bucket'):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
        return [loop, alive_dead]
        
def room13(user_input13, item_list):
        if user_input13.lower() == ('going up'):
                loop = 14
                alive_dead = 'Alive'
        elif user_input13.lower() == ('going east'):
                loop = 12
                alive_dead = 'Alive'
        elif user_input13.lower() == ('kick the bucket'):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
        return [loop, alive_dead]

def room14(user_input14, item_list):
        if user_input14.lower() == ('going down'):
                loop = 13
                alive_dead = 'Alive'
        elif user_input14.lower() == ('kick the bucket'):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
        return [loop, alive_dead]

def room15(user_input15, item_list):
        if user_input15.lower() == ('going north'):
                loop = 10
                alive_dead = 'Alive'
        elif user_input15.lower() == ('going south'):
                loop = 16
                alive_dead = 'Alive'
        elif user_input15.lower == ('going east'):
                loop = 17
                alive_dead = 'Alive'
        elif user_input15.lower() == ('kick the bucket'):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
        return [loop, alive_dead]

def room16(user_input16, item_list):
        if user_input16.lower() == ('going north'):
                loop = 15
                alive_dead = 'Alive'
        else:
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)
                
        return [loop, alive_dead]

def room17(user_input17, item_list):
        if user_input17.lower == ('going west'):
                loop = 15
                alive_dead = 'Alive'
        else:
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)

        return [loop, alive_dead]




