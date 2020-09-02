from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


print(room['foyer'])
print(room['foyer'].n_to)
print(room['foyer'].s_to)
print(room['foyer'].e_to)


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player_name = input('Who dares seek the treasure?  ')
# player_name = "wade watts"
player1 = Player(player_name, room["outside"])



# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
playing = True

while playing:
    print(player1)
    print()
    direction = input("\nWhere do you want to move ?  [n] north, [s] south, [e] east, [w] west, [q] quit ...: ")

    if direction == "q":
        print('Thank you for playing, come again soon')
        playing = False
    elif direction == "n":
        print("\n ===moving North=== \n")
        if player1.current_room.name == "Outside Cave Entrance":
            player1.current_room = room["foyer"]
        elif player1.current_room.name == "Foyer":
            player1.current_room = room["overlook"]
        elif player1.current_room.name == 'Narrow Passage':
            player1.current_room = room["treasure"]
        else:
            print("There is no room in that direction \n")
    elif direction == "s":
        print("\n ===moving South===\n")
        if player1.current_room.name == "Foyer":
            player1.current_room = room["outside"]
        elif player1.current_room.name == "Grand Overlook":
            player1.current_room = room["foyer"]
        elif player1.current_room.name == 'Treasure Chamber':
            player1.current_room = room["narrow"]
        else:
            print("There is no room in that direction \n")
    elif direction == "e":
        print("\n ===moving East===\n")
        if player1.current_room.name == "Foyer":
            player1.current_room = room["narrow"]
        else:
            print("There is no room in that direction \n")
    elif direction == "w":
        print("\n ===moving West=== \n")
        if player1.current_room.name == "Narrow Passage":
            player1.current_room = room["foyer"]
        else:
            print("There is no room in that direction\n")
    else:
        print("\nYou Can only move [n] north, [s] south, [e] east, [w] west, [q] quit.  Where do you want to move ?      ")