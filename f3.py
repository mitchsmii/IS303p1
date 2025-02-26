#3. Display list of all teams and allow the user to choose a team using a menu. 
# Call the function again to let the user choose the opponent but do not display 
# the team they chose previously. Remove that team from the list. Allow the user 
# to select an opponent, and return team name. This function should receive a 
# parameter but give it a default value if none is passed. You can use this 
# function for both choosing the home team and the opponent team.

from main import *
from f2 import Menu
from displayGameIntro import displayGameIntro

def fullGame():
    
    count = 1
    while count != 0:
        if sMenuChoice == 1:
            print("Choose your team")
        elif sMenuChoice == 2:
            print("Choose opponent team")
        elif sMenuChoice == 3:
            print("Show rules again")
            displayGameIntro()
            Menu()
        elif sMenuChoice == 4:
            print("Play again")
        elif sMenuChoice == 5:
            print("quit")
            count = 0
        
fullGame()