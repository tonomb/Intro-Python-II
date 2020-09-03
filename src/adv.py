import os
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons, There is a mysterious land to the south. Only with the power of the ring can you enter"),

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

    'morodor': Room("Morodor", """You've entered the relm of sauron, head further south ro reach mount Doom"""),

    'mountain': Room("Mount Doom", """You've entered Mount Doom, It was here that Sauron forged the One Ring"""),

    'hogwarts': Room("Hogwarts Castle", """Your a wizard!!!! I hope you have your wand with you, It´s not safe"""),
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
room['morodor'].s_to = room['mountain']

# adding items to rooms

room["outside"].items.append(Item("Torch", "Lights up the darkest places"))
room["foyer"].items.append(Item("Shield", "level 1"))
room["foyer"].items.append(Item("Sword", "The sword of the last kings"))
room["overlook"].items.append(Item("Bow", "This bow never misses it´s target"))
room["narrow"].items.append(Item("Wand", "This item doesn´t belong in this fantasy"))
room["treasure"].items.append(Item("Ring", "Forged in the fires of mount doom"))


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# player_name = input('Who dares seek the treasure?  ')
player_name = "wade watts"
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
    # os.system('clear')
    player1.location()
    print()
    if len(player1.current_room.items) > 0:
        print(f"You see {len(player1.current_room.items)} items\n")
        player1.current_room.print_items()
    else:
        print("There are no items in this room")
    print()



    if player1.current_room.name == 'Mount Doom':
        decision = input('Would you like to cast the ring into the fire ? [y] yes [n] no...: ')
        if decision == 'y':
            print('You have destoyed the ring')
            playing = False
        elif decision =='n':
            print('May the odds be in your favor')
            player1.move(room['hogwarts'])
        else:
            print('That is not a valid decision')
    else:
        pass

    full_command = input("\nWhat would you like to do?---->  ")

    split_command = full_command.split()
    command = split_command[0]

    
    # movement
    if command == "q":
        print('Thank you for playing, come again soon')
        playing = False
    elif command == "n":
        print("\n ===moving North=== \n")
        try:
            player1.move(player1.current_room.n_to)
        except AttributeError:
            print("There is no room in that direction \n")
    elif command == "s":
        print("\n ===moving South===\n")
        try:
            player1.move(player1.current_room.s_to)
        except AttributeError:
            print("There is no room in that direction \n")
    elif command == "e":
        print("\n ===moving East===\n")
        try:
            player1.move(player1.current_room.e_to)
        except AttributeError:
            print("There is no room in that direction \n")
    elif command == "w":
        print("\n ===moving West=== \n")
        try:
            player1.move(player1.current_room.w_to)
        except AttributeError:
            print("There is no room in that direction \n")
    # actions
    elif command == 'take':
        if len(split_command) == 2:
            item = split_command[1]
            if len(player1.current_room.items) > 0:
                for room_item in player1.current_room.items:
                    if room_item.name.lower() == item.lower():
                        player1.take_item(room_item)
                        print(f"you have picked up the {room_item.name}")
                        player1.current_room.remove_item(room_item)
                        if room_item.name.lower() == 'ring':
                            player1.move(room['outside'])
                            print("\nA magic land appears south")
                            room['outside'].s_to = room['morodor']
                        else:
                            pass
                    else:
                        print("That items does not exist in this room")
            else:
                print("That items does not exist in this room 2")
        else:
            print("\nThat is not a valid command")
    elif command == 'drop':
        if len(split_command) == 2:
            item = split_command[1]
            if len(player1.inventory) > 0:
                for player_item in player1.inventory:
                    if player_item.name.lower() == item.lower():
                        player1.drop_item(player_item)
                        print(f"you have dropped the {player_item.name}")
                        player1.current_room.add_item(player_item)
                    else:
                        print("That items does not exist in your inventory")
            else:
                print("That items does not exist in your inventory")
        else:
            print("\nThat is not a valid command")

    # other
    elif command == 'i':
        player1.list_inventory()
    elif command == 'h':
        print(f"==== HELP ==== \nMove: [n] north, [s] south, [e] east, [w] west \nAction: [take] item [drop] item \n[i] inventory [h] help, [q] quit")

    # room mechanics

    else:
        print("\nThat is not a valid command. Would you like some [h] help?")