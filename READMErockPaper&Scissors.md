# TITLE: Rock, Paper, Scissors
-this is a rock-paper-scissors command line game with addittional features like a leaderboard and a "how to play" section.
-the game also made sure to have a limit of attempts per round so as to keep the game intersting. 
--after the limited chances given per round, the winner of the round will be displayed either player or computer.
-the game also keeps a leaderboard of the players and their scores. 


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
-
-the code made use of a modification in play_round() to ask the player if they would like to try again after they lose to the computer. If the player enters "y" the function starts a new round. If the player enters "n" (or any variation of "no"), the gam
e continues as usual. Note that this modification assumes that the player only enters "y" or "n" as a response to the prompt.
-time modification- This modification adds a delay of 0.1 seconds between each letter print using the time.sleep() function. The flush=True argument in the print() function ensures that each letter is imme
diately printed to the console instead of being buffered.

# PROJECT DEPLOYMENT: 


# SOURCES USED FOR THE PROJECT:
-the project made use of Tutorials online as well as code along videos on Youtube. 
    The primary sources used for this project where the follwoing:
    1. How to code Rock, Paper acrissors(beginer Python Tutorial) https://www.youtube.com/watch?v=xRlN8CFJwAM
    2. Rock Paper Scissors- C# - CLI App https://www.youtube.com/watch?v=5A_26sEajTI
    3. How to code a rck paper scissor Game with Python | Programming Tutorial https://www.youtube.com/watch?v=fn68QNcatfo
    4. 


# TESTING AND UNSOLVED BUGS
-the code intially has 15 problems 7 being the line is too long, 6 being expectes 2 blank lines found and 2 being continuation line over-indented for visual indent. 
- after using ideone.com to check the code, there was one error labelled- Traceback (most recent call last):  File "<string>", line 1, in <module>
  File "/usr/lib/python2.7/py_compile.py", line 117, in compile
    raise py_exc
py_compile.PyCompileError:   File "prog.py", line 76
    print(letter, end='', flush=True)- to fix tis code, l reasearched on Stack and found that the error message indicates a SyntaxError at line 76 due to invalid syntax in the print() function. To solve this, the code had to change from /print(letter, end='', flush=True)/ to /print(letter, end='', flush=True) ,/
-the project also used pep8ci.herokuapp.com to test the code and the same erros l found in the codeanywhere are the same l found in the site when validating the code. 
# deployment
-added a new line character text at the end of the line in input method
-created a list of requirements  that our project needs to run.