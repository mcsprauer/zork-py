import items

my_item_list = []

def front_of_house(second):
        status = 'alive'
        room_num = 4
        if second.lower() == ("take mailbox"):
                print("---------------------------------------------------------")
                print("It is securely anchored.")
        elif second.lower() == ("open mailbox"):
                print("---------------------------------------------------------")
                print("Opening the small mailbox reveals a leaflet.")
        elif second.lower() == ("go north"):
                room_num = 1
        elif second.lower() == ("open door"):
                print("---------------------------------------------------------")
                print("The door cannot be opened.")
        elif second.lower() == ("take boards"):
                print("---------------------------------------------------------")
                print("The boards are securely fastened.")
        elif second.lower() == ("look at house"):
                print("---------------------------------------------------------")
                print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
        elif second.lower() == ("go southwest"):
                room_num = 8
        elif second.lower()== 'go east':
                room_num = 14
        elif second.lower() == ("read leaflet"):
                print("---------------------------------------------------------")
                print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
        elif second.lower().startswith("put down"):
                item = items.put_down(second[9:],4)
                my_item_list.remove(item)
        elif second.lower().startswith("pick up"):
                item = items.pick_up(second[8:],4)
                my_item_list.append(item)
        elif second.lower() == ("kick the bucket"):
                status = 'dead'
        else:
                print("---------------------------------------------------------")

        return room_num, status


def north_of_house(north_house_inp):
        status = 'alive'
        room_num = 1
        if north_house_inp.lower() == ("go south"):
                room_num = 4
        elif north_house_inp.lower() == ("swim"):
                print("---------------------------------------------------------")
                print("You don't have a change of clothes and you aren't here on vacation.")
        elif north_house_inp.lower() == ("fish"):
                print("---------------------------------------------------------")
                print("You spend some time fishing but nothing seems to bite.")
        elif north_house_inp.lower().startswith("put down"):
                item = items.put_down(north_house_inp[9:],1)
                my_item_list.remove(item)
        elif north_house_inp.lower().startswith("pick up"):
                item = items.pick_up(north_house_inp[8:],1)
                my_item_list.append(item)
        elif north_house_inp.lower() == ("kick the bucket"):
                status = 'dead'
        else:
                print("---------------------------------------------------------")

        return room_num, status

def southwest_loop(forest_inp):
        status = 'alive'
        room_num = 8
        if forest_inp.lower() == ("go west"):
                print("---------------------------------------------------------")
                print("You would need a machete to go further west.")
        elif forest_inp.lower() == ("go north"):
                print("---------------------------------------------------------")
                print("The forest becomes impenetrable to the North.")
        elif forest_inp.lower() == ("go south"):
                print("---------------------------------------------------------")
                print("Storm-tossed trees block your way.")
        elif forest_inp.lower() == ("go east"):
                room_num = 9
        elif forest_inp.lower().startswith("put down"):
                item = items.put_down(forest_inp[9:],8)
                my_item_list.remove(item)
        elif forest_inp.lower().startswith("pick up"):
                item = items.pick_up(forest_inp[8:],8)
                my_item_list.append(item)
        elif forest_inp.lower() == ("kick the bucket"):
                status = 'dead'
        else:
                print("---------------------------------------------------------")
        return room_num, status

def east_loop_and_grating(grating_inp):
        status = 'alive'
        room_num = 9
        if grating_inp.lower() == ("go south"):
                print("---------------------------------------------------------")
                print("You see a large ogre and turn around.")
        elif grating_inp.lower() == ("descend grating"):
                room_num = 10
        elif grating_inp.lower().startswith("put down"):
                item = items.put_down(grating_inp[9:],9)
                my_item_list.remove(item)
        elif grating_inp.lower().startswith("pick up"):
                item = items.pick_up(grating_inp[8:],9)
                my_item_list.append(item)
        elif grating_inp.lower() == ("kick the bucket"):
                status = 'dead'
        else:
                print("---------------------------------------------------------")
        return room_num,status

def grating_loop_and_cave(cave_inp):
        status = 'alive'
        room_num = 10
        if cave_inp.lower() == ("descend staircase"):
                room_num = 11
        elif cave_inp.lower() == ("take skeleton"):
                print("---------------------------------------------------------")
                print("Why would you do that? Are you some sort of sicko?")
        elif cave_inp.lower() == ("smash skeleton"):
                print("---------------------------------------------------------")
                print("Sick person. Have some respect mate.")
        elif cave_inp.lower() == ("light up room"):
                print("---------------------------------------------------------")
                print("You would need a torch or lamp to do that.")
        elif cave_inp.lower() == ("break skeleton"):
                print("---------------------------------------------------------")
                print("I have two questions: Why and With What?")
        elif cave_inp.lower() == ("go down staircase"):
                room_num = 11
        elif cave_inp.lower() == ("enter maze"):
                room_num = 15
        elif cave_inp.lower().startswith("put down"):
                item = items.put_down(cave_inp[9:],10)
                my_item_list.remove(item)
        elif cave_inp.lower().startswith("pick up"):
                item = items.pick_up(cave_inp[8:],10)
                my_item_list.append(item)
        elif cave_inp.lower() == ("kick the bucket"):
                status = 'dead'
        elif cave_inp.lower() == ("scale staircase"):
                room_num = 11

        else:
                print("---------------------------------------------------------")
        return room_num,status

def kitchen(kitchen_inp):
        status = 'alive'
        room_num = 12
        if kitchen_inp.lower() == "go up":
                room_num = 13
        elif kitchen_inp.lower() == "go east":
                room_num = 14
        elif kitchen_inp.lower().startswith("put down"):
                item = items.put_down(kitchen_inp[9:],12)
                my_item_list.remove(item)
        elif kitchen_inp.lower().startswith("pick up"):
                item = items.pick_up(kitchen_inp[8:],12)
                my_item_list.append(item)
        elif kitchen_inp.lower() == ("kick the bucket"):
                status = 'dead'
        else:
                print("---------------------------------------------------------")
        return room_num,status


def attic(attic_inp):
        status = 'alive'
        room_num = 13
        if attic_inp.lower() == 'go down':
                room_num = 12
        elif attic_inp.lower().startswith("put down"):
                item = items.put_down(attic_inp[9:],13)
                my_item_list.remove(item)
        elif attic_inp.lower().startswith("pick up"):
                item = items.pick_up(attic_inp[8:],13)
                my_item_list.append(item)
        elif attic_inp.lower() == ("kick the bucket"):
                status = 'dead'
        else:
                print("---------------------------------------------------------")
        return room_num,status

def back_of_house(back_of_house_inp):
        status = 'alive'
        room_num = 14
        if back_of_house_inp.lower() == 'go south':
                room_num = 4
        elif back_of_house_inp.lower() == 'go west':
                print("---------------------------------------------------------")
                print('Opening a rickety window you climb into the house.')
                room_num = 12
        elif back_of_house_inp.lower() == 'enter bouncy house':
                room_num = 17
        elif back_of_house_inp.lower().startswith("put down"):
                item = items.put_down(back_of_house_inp[9:],14)
                my_item_list.remove(item)
        elif back_of_house_inp.lower().startswith("pick up"):
                item = items.pick_up(back_of_house_inp[8:],14)
                my_item_list.append(item)
        elif back_of_house_inp.lower() == ("kick the bucket"):
                status = 'dead'
        else:
                print("---------------------------------------------------------")
        return room_num,status

def maze_entrance(maze_inp):
        status = 'alive'
        room_num = 15
        if maze_inp.lower() == 'enter cave':
                room_num = 10
        elif maze_inp.lower() == 'go south':
                room_num = 16
        elif maze_inp.lower().startswith("put down"):
                item = items.put_down(maze_inp[9:],10)
                my_item_list.remove(item)
        elif maze_inp.lower().startswith("pick up"):
                item = items.pick_up(maze_inp[8:],10)
                my_item_list.append(item)
        elif maze_inp.lower() == ("kick the bucket"):
                status = 'dead'
        else:
                print("---------------------------------------------------------")
        return room_num,status

def maze_interior(maze_inp):
        status = 'alive'
        room_num = 16
        if maze_inp.lower() == 'go north':
                room_num = 15
        elif maze_inp.lower().startswith("put down"):
                item = items.put_down(maze_inp[9:],16)
                my_item_list.remove(item)
        elif maze_inp.lower().startswith("pick up"):
                item = items.pick_up(maze_inp[8:],16)
                my_item_list.append(item)
        elif maze_inp.lower() == ("kick the bucket"):
                status = 'dead'
        else:
                if 'lantern' in my_item_list:
                        print("Watch out there is the GRUE!! Go back!!")
                else:
                        print("You got eaten by the GRUE!!! You're dead my friend.:(")
                        status = 'dead'
        return room_num,status

def bouncy_house(bouncy_inp):
        status = 'alive'
        room_num = 17
        if bouncy_inp.lower() == 'do trick':
                print("---------------------------------------------------------")
                print('SWEET TRICK!')
        elif bouncy_inp.lower() == 'teleport':
                room_num = 13
        elif bouncy_inp.lower().startswith("put down"):
                item = items.put_down(bouncy_inp[9:],17)
                my_item_list.remove(item)
        elif bouncy_inp.lower().startswith("pick up"):
                item = items.pick_up(bouncy_inp[8:],17)
                my_item_list.append(item)
        elif bouncy_inp.lower() == ("kick the bucket"):
                status = 'dead'
        else:
                print('A meteor destroyed the bouncy house. You dead.')
                status = 'dead'
        return room_num,status       
                

def end_of_game(last_inp):
        status = 'alive'
        room_num = 11
        if last_inp.lower() == ("open trunk"):
                print("---------------------------------------------------------")
                print("You have found the Jade Statue and have completed your quest!")
        elif last_inp.lower().startswith("put down"):
                item = items.put_down(last_inp[9:],11)
                my_item_list.remove(item)
        elif last_inp.lower().startswith("pick up"):
                item = items.pick_up(last_inp[8:],11)
                my_item_list.append(item)
        elif last_inp.lower() == ("kick the bucket"):
                status = 'dead'
        else:
                print("---------------------------------------------------------")

        return room_num,status



