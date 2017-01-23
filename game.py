from random import randint

# Welcome message
print ("\nThis is a multiplayer guessing game. The number will be between 1 and 100.")

# Set things up
players = []                        # create empty list of players
current_player = 1                  # start current player as player 1
random_number = randint(1, 100)     # generate random number
guess = False                       # initialize guess as false

# Get player info
num_players = int(input("\nHow many players are there? "))
while len(players) < num_players:
    player_name = input("\nEnter player %d's name: " % (len(players) + 1))
    players.append(player_name)

# Function to compare guess with random_number
def compare(num):
    if num == random_number:
        print("\n*** Congrats, %s! You guessed the number. You win! ***" % (players[current_player - 1]))
    elif num > random_number:
        print("\nLower...")
    elif num < random_number:
        print("\nHigher...")
    else:
        print("\n*** Well, something didn't work! ***")

# The game
while guess != random_number:
    # Ask for player's guess
    guess = int(input("\n%s, what is your guess? " % (players[current_player - 1])))

    # Call function to compare guess with random_number
    compare(guess)

    # Change current_player
    if current_player < num_players:
        current_player += 1
    else:
        current_player = 1
