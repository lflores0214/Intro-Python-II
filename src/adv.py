import os
from room import Room
from player import Player
from item import Item, Light, Food

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

outside = room['outside']
foyer = room['foyer']
overlook = room['overlook']
narrow = room['narrow']
treasure = room['treasure']

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

## Items
torch = Light("Torch", "a piece of wood with cloth wrapped around the end.", False)
apple = Food("Apple", "A juicy red apple", 20)

room['outside'].items = [apple]
room['foyer'].items = [torch]

# Make a new player object that is currently in the 'outside' room.
player = Player(input("Enter a name >> ").capitalize(), outside)

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


def welcome_screen():
    print('===========================================')
    print('//        Welcome to Adventure Game!     \\\\')
    print('===========================================')
    print('|           inputs: (n)orth,              |')
    print('|                   (s)outh,              |')
    print('|                   (e)ast,               |')
    print('|                   (w)est,               |')
    print('|                   (h)elp,               |')
    print('|                   (q)uit,               |')
    print('|                   (i)nventory           |')
    print('|                   (c)heck room          |')
    print('===========================================')
    print('\n\n')
    print(f"{player.name}'s current location: {player.room.name} \n")
    print(f"{player.room.description} \n")


def help_screen():
    print('===========================================')
    print('|           inputs: (n)orth,              |')
    print('|                   (s)outh,              |')
    print('|                   (e)ast,               |')
    print('|                   (w)est,               |')
    print('|                   (h)elp,               |')
    print('|                   (q)uit,               |')
    print('|                   (i)nventory           |')
    print('|                   (c)heck room          |')
    print('===========================================')


os.system('clear')
welcome_screen()

directions = ["n", "s", "w", "e"]

# LOOP
while True:
    # Print name of current room

    user_input = input("Type your command >> ").lower()
    if user_input in directions:
        player.travel(player.room, user_input)
    elif user_input == "q":
        print("Hope you had fun!")
        break
    elif user_input == "h":
        help_screen()
    elif user_input == "i":
        player.check_inventory()
    elif user_input == "c":
        player.room.check_items()
    else:
        print("invalid input")
