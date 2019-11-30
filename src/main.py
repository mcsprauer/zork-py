# Main game file

import zork

def get_input():
        return input('What do you do? ')
    
def PrintOutput(s):
    print("OUTPUT", s)
    
def Play_Zork():
    room = 4
    print("---------------------------------------------------------")
    print("Welcome to Zork - The Unofficial Python Version.")

    while True:
        # First Input room
        if room == 4:
            print("---------------------------------------------------------")
            print("You are standing in an open field west of a white house, with a boarded front door.")
            print("You can see a small lake to the north.")
            print("(A secret path leads southwest into the forest.)")
            print("There is a Small Mailbox.")
            room,stat = zork.front_of_house(get_input())
            if stat == 'dead':
                break

        # North of House
        elif room == 1:
            print("---------------------------------------------------------")
            print("You find yourself at the edge of a beautiful lake aside rolling hills.")
            print("A small pier juts out into the lake.")
            print("A fishing rod rests on the pier.")
            print("(You can see a white house in the distance to the south.)")
            room,stat = zork.north_of_house(get_input())
            if stat == 'dead':
                break

        # Southwest loop
        elif room == 8:
            print("---------------------------------------------------------")
            print("This is a forest, with trees in all directions. To the east, there appears to be sunlight.")
            room,stat = zork.southwest_loop(get_input())
            if stat == 'dead':
                break

        # East loop and Grating Input
        elif room == 9:
            print("---------------------------------------------------------")
            print("You are in a clearing, with a forest surrounding you on all sides. A path leads south.")
            print("There is an open grating, descending into darkness.")
            room,stat = zork.east_loop_and_grating(get_input())
            if stat == 'dead':
                break

        # Grating loop and Cave Input
        elif room == 10:
            print("---------------------------------------------------------")
            print("You are in a tiny cave with a dark, forbidding staircase leading down.")
            print("There is a skeleton of a human male in one corner.")
            print('You see the entrance to a weird looking maze')
            room,stat = zork.grating_loop_and_cave(get_input())
            if stat == 'dead':
                break

        #Kitchen
        elif room == 12:
            print("---------------------------------------------------------")
            print('You find yourself in a dimly lit kitchen with dust covering the floor.')
            print('A lantern rests on the kitchen island.')
            print('A set of stairs leads up to another room.')
            room,stat = zork.kitchen(get_input())
            if stat == 'dead':
                break
        #Back of the house
        elif room == 14:
            print("---------------------------------------------------------")
            print('You find yourself at the back of the house.')
            print('There is a rickety window to your west')
            print('To the south there is a pathway.')
            print('There seems to be a pretty normal looking bouncy house')
            room,stat = zork.back_of_house(get_input())
            if stat == 'dead':
                break
            
        #Attic
        elif room == 13:
            print("---------------------------------------------------------")
            print('You find yourself is a disgusting place with cobwebs.')
            room,stat = zork.attic(get_input())
            if stat == 'dead':
                break
        #Maze entrance
        elif room == 15:
            print("---------------------------------------------------------")
            print('You are at the entrance of a dark, creepy maze')
            print('You can brave the maze if you go south')
            room,stat = zork.maze_entrance(get_input())
            if stat == 'dead':
                break

        #Maze interior
        elif room == 16:
            print("---------------------------------------------------------")
            print('You are even deeper in the maze!')
            room,stat = zork.maze_interior(get_input())
            if stat == 'dead':
                break

        #Bouncy House
        elif room == 17:
            print("---------------------------------------------------------")
            print('Beware the bounce')
            print('Do a trick')
            room,stat = zork.bouncy_house(get_input())
            if stat == 'dead':
                break
            


        # End of game
        elif room == 11:
            print("---------------------------------------------------------")
            print("You have entered a mud-floored room.")
            print("Lying half buried in the mud is an old trunk, bulging with jewels.")
            room,stat = zork.end_of_game(get_input())
            break

    if stat == 'dead':
        print("---------------------------------------------------------")
        print("You die.")
        print("---------------------------------------------------------")
    done_inp = input("Do you want to continue? Y/N ")
    if done_inp.lower() == ("n"):
            return
    if done_inp.lower() == ("y"):
            Play_Zork()
				    
#Main
Play_Zork()
print('Game Over')
