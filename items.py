# Items that exist in each room and the functions you can use to interact with them

#TODO Define items in each room
room0items = []
room1items = []
room2items = []
room3items = []
room4items = []
# ...

allItems = [room0items, room1items, room2items, room3items, room4items]

# Returns item to be added to inventory if it exists in this room and removes it from the list of items in the coom
def pick_up(itemName, roomNum):
    if itemName in allItems[roomNum]:
        allItems[roomNum].remove(itemName)
        return itemName
    else:
        print("Not a valid item to pick up")
        return -1

# Puts the item down in the current room, adds it to the item list of the current room, 
# and returns 0 to indicate that it was successfully removed.
def put_down(itemName, roomNum):
    print("You put down the ", itemName)
    # TODO Add item to room item list
    return 0