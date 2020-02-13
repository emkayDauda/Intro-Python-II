from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside the Cave Entrance",
                     "North of you, the cave mount beckons", 'outside'),

    'foyer':    Room("in the Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", 'foyer'),

    'overlook': Room("at the Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", 'overlook'),

    'narrow':   Room("in the Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", 'narrow'),

    'treasure': Room("at the Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", 'treasure'),
}


# Link rooms together

room['outside'].w_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].w_to = room['overlook']
room['foyer'].a_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].d_to = room['foyer']
room['narrow'].w_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

def startSession():
    heroName = input('Welcome...\n\nPlease give your hero a name: ')
    currentPlayer = Player(heroName, room['outside'])
    
    firstMove = input(f"""\n\nYou may begin, {currentPlayer.name}. You are in {currentPlayer.room.name}.
{currentPlayer.room.desc}. What shall your first move be?\n
Your options are: "w" to advance, "s" to retreat, "a" to strafe left and "d" to strafe right. 
Decide now: """)
    maintainSession(currentPlayer, firstMove)
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




def hasPath(player, direction):
    path = f'{direction}_to'
    # hasRoom = hasattr(room[player.room.key], path)
    nextRoom = getattr(room[player.room.key], path)
    if (nextRoom != {}):
        player.room = nextRoom
        return True
    else: return False

def moveIsCardinal(move):
    return move.lower() == 'w' or move.lower() == 's' or move.lower() == 'a' or move.lower() == 'd'


def maintainSession(player, firstMove):
    playing = True
    nextMove = firstMove
    while (playing):
        if (moveIsCardinal(nextMove)):
            if (hasPath(player, nextMove)):
                print(f"\nSuccess, you are {player.room.name}. {player.room.desc}")
                nextMove = input("\nWhat shall your next move be? ")
            else: 
                nextMove = input("\nHow hard can this be? Make a valid move: ")
        else:
            if (nextMove.lower() == 'q'):
                playing = False
            else:
                nextMove = input("\nFailure\n\nChoose one of the four cardinals, please w, s, a or d: ")
    
    print('\n\nThank you for playing this time.\n\n')


startSession()