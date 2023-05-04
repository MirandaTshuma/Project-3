# Importing random and time modules to generate random choices for the player
import random
import time
# Initializing an empty dictionary for the leaderboard to keep track of wins, ties and loses
leaderboard = {}
# Function to display the main menu
def show_menu():
    print("Welcome to Rock-Paper-Scissors!😁")
    print("Enter your choice (R/P/S) and see if you can beat the computer!😛")
    print("\n1. Play a round")
    print("2. View leaderboard")
    print("3. How to play")
    print("4. Quit at any moment")
# function to play a single round
def play_round(player_name):
    valid_choices = ["R", "P", "S"]
    player_choice = ""
    # loop for until player enters a valid choice
    while player_choice not in valid_choices:
        player_choice = input(player_name + ", enter your choice (R/P/S) or type 'quit' to exit: ").upper()
        if player_choice == 'QUIT':
            print("\nThanks for playing!👋")
            exit()
     # to randomly select the computer's choice
    computer_choice = random.choice(valid_choices)
    # to determine the winner of the round
    winner = determine_winner(player_choice, computer_choice)
     # to update the leaderboard based on the winner between computer and player
    if winner == player_name:
        print("\nCongratulations, " + player_name + ", you win!😊")
        leaderboard[player_name] = leaderboard.get(player_name, {'wins': 0, 'losses': 0, 'ties': 0})
        leaderboard[player_name]['wins'] += 1
    elif winner == "Computer":
        print("\nSorry, the computer wins.😔")
        leaderboard["Computer"] = leaderboard.get("Computer", {'wins': 0, 'losses': 0, 'ties': 0})
        leaderboard["Computer"]['wins'] += 1
    else:
        print("\nIt's a tie!")
        leaderboard[player_name] = leaderboard.get(player_name, {'wins': 0, 'losses': 0, 'ties': 0})
        leaderboard[player_name]['ties'] += 1
        leaderboard["Computer"] = leaderboard.get("Computer", {'wins': 0, 'losses': 0, 'ties': 0})
        leaderboard["Computer"]['ties'] += 1
# to display the leaderboard
def view_leaderboard():
    print("\nLeaderboard:")
    print("{:<10} {:<10} {:<10} {:<10}".format('Player', 'Wins', 'Losses', 'Ties'))
    print("-" * 40)
    for player, scores in leaderboard.items():
        print("{:<10} {:<10} {:<10} {:<10}".format(player, scores['wins'], scores['losses'], scores['ties']))
# function to determine the winner of a round played
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie" #if user and computer both select the same choice
    elif (player_choice == "R" and computer_choice == "S") \
         or (player_choice == "S" and computer_choice == "P") \
         or (player_choice == "P" and computer_choice == "R"):
        return "Player"
    else:
        return "Computer"
# Function to display the rules of the game
def how_to_play():
    print("\nHow to Play:")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")
    print("Enter your choice (R/P/S) and see if you can beat the computer!")

while True:
    show_menu()
    # gets the user's choice from the input
    choice = input("\nEnter your choice (1/2/3/4):")
    # for when the user chooses to play the game,game should ask for their name and play only 5 rounds
    if choice == "1":
        player_name = input("Enter your name: ")
        for j in range(5):
             # a call function to play a round of rock-paper-scissors
            play_round(player_name)
            data_str = input("Enter your data here")
            # to add delay before displaying the next round
            for letter in "Round " + str(j+1) + "...":
                print(letter, end='', flush=True) ,
            time.sleep(0.5)
    # display leaderboard, if player requests for it
    elif choice == "2":
        view_leaderboard()
    # display rules if player chooses to learn how to play by displaying instructions
    elif choice == "3":
        how_to_play()
    # when player chooses to exit the game, game should break out of the loop and end the program and display a farewell message
    elif choice == "4":
        print("\nThanks for playing!👋")
        break
    # If player enters an invalid choice, prompt to tell them to try again
    else:
        print("\nInvalid choice. Please try again.")

    # this is to add a delay before displaying the menu again
    time.sleep(0.5)
