import random
import time

leaderboard = {}
def show_menu():
    print("Welcome to Rock-Paper-Scissors!😁")
    print("Enter your choice (R/P/S) and see if you can beat the computer!😛")
    print("\n1. Play a round")
    print("2. View leaderboard")
    print("3. How to play")
    print("4. Quit at any moment")

def play_round(player_name):
    valid_choices = ["R", "P", "S"]
    player_choice = ""
    while player_choice not in valid_choices:
        player_choice = input(player_name + ", enter your choice (R/P/S) or type 'quit' to exit: ").upper()
        if player_choice == 'QUIT':
            print("\nThanks for playing!👋")
            exit()
    computer_choice = random.choice(valid_choices)
    winner = determine_winner(player_choice, computer_choice)

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

def view_leaderboard():
    print("\nLeaderboard:")
    print("{:<10} {:<10} {:<10} {:<10}".format('Player', 'Wins', 'Losses', 'Ties'))
    print("-" * 40)
    for player, scores in leaderboard.items():
        print("{:<10} {:<10} {:<10} {:<10}".format(player, scores['wins'], scores['losses'], scores['ties']))

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif (player_choice == "R" and computer_choice == "S") \
         or (player_choice == "S" and computer_choice == "P") \
         or (player_choice == "P" and computer_choice == "R"):
        return "Player"
    else:
        return "Computer"

def how_to_play():
    print("\nHow to Play:")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")
    print("Enter your choice (R/P/S) and see if you can beat the computer!")

while True:
    show_menu()
    choice = input("\nEnter your choice (1/2/3/4): ")

    if choice == "1":
        player_name = input("Enter your name: ")
        for j in range(5):
            play_round(player_name)

            # Add a delay before displaying the next round
            for letter in "Round " + str(j+1) + "...":
                print(letter, end='', flush=True) ,
            time.sleep(0.5)
    elif choice == "2":
        view_leaderboard()

    elif choice == "3":
        how_to_play()

    elif choice == "4":
        print("\nThanks for playing!👋")
        break
    else:
        print("\nInvalid choice. Please try again.")

    # Add a delay before displaying the menu again
    time.sleep(0.5)
