# TITLE: Rock, Paper, Scissors
-this is a simple rock-paper-scissors command line game with addittional features like a leaderboard and a "how to play" section.
-the game also made sure to have a limit of attempts per round so as to keep the game intersting. 
-after the limited chances given per round, the winner of the round will be displayed either player or computer.
-the game also keeps a leaderboard of the players and their scores. 

# Existing Features
1. Welcome to Rock-Paper-Scissors!😁
    -this is the first line of the game. It serves as an introduction to the player on the game to be played. Emojis were added to made the game interactive
2. Enter your choice (R/P/S) and see if you can beat the computer!😛
    -this is a prompt for the player to choose their choice between Rock(r), Paper (p) and Scissor(s)
# HOW TO PLAY:
-the main menu will be displayed, providing 
1. the instructions on how to play the game
2. Main Menu
    i. Play a round
    ii. View Leaderboard
    iii. How to play
    iv. Quit
    -choices will be displayed in abbreviations for the player to choose and continue with the game. 


# PROJECT DEVELOPMENT:
-the project uses the show menu function to display options for the player. Using this menu, the player is able to select what they desire and go ahead and play, view the leaderboard or learn the rules or quit. 
-the project makes use of the play_round(player_name) function which is called when the user selects the "Play a round" option from the main menu. It prompts the player to enter their choice (either "R", "P", or "S") and checks that the input is valid. If the player enters "quit", the game ends. 
-the determine determine_winner(player_choice, computer_choice) function is to determine the winner of the round based on the game's rules.
-the code made use of a modification in play_round() to ask the player if they would like to try again after they lose to the computer. If the player enters "y" the function starts a new round. If the player enters "n" (or any variation of "no"), the game continues as usual. Note that this modification assumes that the player only enters "y" or "n" as a response to the prompt and no other choice will be allowed.
-time modification- This modification adds a delay of 0.1 seconds between each letter print using the time.sleep() function. The flush=True argument in the print() function ensures that each letter is imme
diately printed to the console instead of being buffered.

# SOURCES USED FOR THE PROJECT:
-the project made use of Tutorials online as well as code along videos on Youtube. 
    The primary sources used for this project where the follwoing:
    1. "Rock, Paper, Scissors" Python tutorial on Codecademy: This tutorial providesd a step-by-step instructions for creating a text-based version of the game in Python.
    1. How to code Rock, Paper acrissors(beginer Python Tutorial) https://www.youtube.com/watch?v=xRlN8CFJwAM - this tutorial was used for the section of determing the winner between the player and the computer. 
    -this tutorial was also used for the while loop to achieve the wins necessary.
    2. Rock Paper Scissors- C# - CLI App https://www.youtube.com/watch?v=5A_26sEajTI
    3. How to code a rock paper scissor Game with Python | Programming Tutorial https://www.youtube.com/watch?v=fn68QNcatfo
    -this tutorial was used inwriting the logic in the creation f the game using he loop to ensure that the player plays again. This loop operates on the premise that a round should be a game played 5 times. 
    4. Enrolled in an online tutorial course for better understanding of the language.
    5. Python.org- this website was used in conjuction with tutorials to better understand the coding language as well as expand the information given on the course. While using the library for the below:
    6. GeeksforGeeks- was used to verify and understand the functions and the language provided in the course and in some expamples used. While the project made use of the functions that were understandable to the writer. 


# TESTING AND UNSOLVED BUGS
-the code intially has 15 problems 7 being the line is too long, 6 being expectes 2 blank lines found and 2 being continuation line over-indented for visual indent. 
- after using ideone.com to check the code, there was one error labelled- Traceback (most recent call last):  File "<string>", line 1, in <module>
  File "/usr/lib/python2.7/py_compile.py", line 117, in compile
    raise py_exc
py_compile.PyCompileError:   File "prog.py", line 76
    print(letter, end='', flush=True)- to fix tis code, l reasearched on Stack and found that the error message indicates a SyntaxError at line 76 due to invalid syntax in the print() function. To solve this, the code had to change from /print(letter, end='', flush=True)/ to /print(letter, end='', flush=True) ,/
-the project also used pep8ci.herokuapp.com to test the code and the same erros l found in the codeanywhere are the same l found in the site when validating the code. 

# PROJECT DEPLOYMENT: 
-as per project deployment guidance, this project skipped adding a new line character at the  end of the text inside the input method /n. When tested, the statement Enter your Choice(1/2/3/4): was also displaying /n which did not look appealing. 
-List of requirements was skipped as the code only uses two standard Python modules (random and time) which are included in the standard library and do not require any external dependencies.
    i. Project Settings: Added the buildpack python and nodejs to handle the mock terminal code provided in the source code amking sure that python is first followed by nodejs.
    ii. Deploy- chose Github as the deployment method and connecting Heroku App with the project on Github
    iii.Manually deployed the project. The app was successfuly deployed. 
# Addittional comments
-only a few commits have been done because code was copid from the first initial project when faced with a challenge of a the initial project labelled was not opening on Code Anywhere