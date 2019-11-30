# Items that exist in each room and the functions you can use to interact with them

#Define items in each room
room0items = []
room1items = ['fishing rod']
room2items = []
room3items = []
room4items = []
room5items = []
room6items = []
room7items = []
room8items = []
room9items = []
room10items = ['skeleton']
room11items = []
room12items = ['lantern']
room13items = []
room14items = []
room15items = []
room16items = []
room17items = []
# ...

allItems = [room0items, room1items, room2items, room3items, room4items,
            room5items, room6items, room7items, room8items, room9items,
            room10items, room11items, room12items, room13items, room14items,
            room15items, room16items]

# Returns item to be added to inventory if it exists in this room and removes it from the list of items in the coom
def pick_up(itemName, roomNum):
    if itemName in allItems[roomNum]:
        allItems[roomNum].remove(itemName)
        print("You picked up the %s" % itemName)
        return itemName
    else:
        print("Not a valid item to pick up")
        return -1

# Puts the item down in the current room, adds it to the item list of the current room, 
# and returns 0 to indicate that it was successfully removed.
def put_down(itemName, roomNum):
    if itemName != '':
        print("You put down the ", itemName)
        allItems[roomNum].append(itemName)
    return itemName

