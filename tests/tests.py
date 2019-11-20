# This python script can be run to test various rooms within the game to ensure the correct output

import zork

def testRoom0():
    s = "go north"
    assert (1, zork.Room0(s))

def testNorthRoom():
    s = "fish"
    assert(1, zork.NorthRoom(s))

### Stest various room inputs