# [Creator name]
# Edited by Joseph Xiong, Carson Hendrix

# 3. Display list of all teams and allow the user to choose a team using a menu. 
# Call the function again to let the user choose the opponent but do not display 
# the team they chose previously. Remove that team from the list. Allow the user 
# to select an opponent, and return team name. This function should receive a 
# parameter but give it a default value if none is passed. You can use this 
# function for both choosing the home team and the opponent team.

from f2 import Menu
from displayGameIntro import displayGameIntro

def fullGame(sMenuChoice):

    # Team list
    teamList = ["BYU", "UVU", "SUU", "Utah State", "University of Utah"]

    # Default team is BYU
    iHomeTeam = 0
    sHomeTeam = teamList[iHomeTeam]
    
    bFullGameQuit = False

    #loop until they want to get out of this menu
    while bFullGameQuit == False:
        if sMenuChoice == 1:

        # Choose home team
            bHomeTeamQuit = False

            # Choosing team only quits when bHomeTeamQuit is True
            while bHomeTeamQuit == False :
                # Exception handling
                try :
                    iHomeTeam = int(input(f"Choose your team:\n 1. BYU\n 2. UVU\n 3. SUU\n 4. Utah State\n 5. University of Utah\n Who do you want your home team to be? (Enter a number 1-5): "))

                    if iHomeTeam in range(0, 6) :
                        bHomeTeamQuit = True
                    else :
                        print("Please enter a number between 1-5.\n")

                except ValueError :
                    print("\nPlease choose a number between 1-5.\n")
                except IndexError :
                    print("Please choose a number between 1-5.\n")
            
            # Assigns sHomeTeam to user's team choice and prints the user's team choice
            sHomeTeam = teamList[iHomeTeam - 1]
            print(f"Your team is {sHomeTeam}.")
            sMenuChoice = Menu()

        elif sMenuChoice == 2:

        # Choose opponents team
            teamList.pop(iHomeTeam - 1)
            bOppTeamQuit = False

            # Choosing opponent only quits when bOppTeamQuit is True
            while bOppTeamQuit == False:
                print("Choose opponent team: ")

                for i, team in enumerate(teamList):
                    print(f"{i+1}. {team}\t")
                # Exception handling
                try:
                    iAwayTeam = int(input("Who do you want your opponent team to be? (Enter a number 1-4): "))

                    if iAwayTeam in range(0, 5) :
                        bOppTeamQuit = True
                    else: 
                        print("\nPlease choose a number between 1-4.\n")

                except ValueError :
                    print("\nPlease choose a number between 1-4.\n")
                except IndexError :
                    print("Please choose a number between 1-4.\n")
                    bOppTeamQuit = True

            sAwayTeam = teamList[iAwayTeam - 1]

            # THEY CAN ONLY LEAVE THE LOOP IF THEY QUIT OR CHOOSE THEIR TEAM AND OPP TEAM
            return sHomeTeam, sAwayTeam
        
        elif sMenuChoice == 3:

        #show rules again
            displayGameIntro()
            sMenuChoice = Menu()

        #im pretty sure that this part doesnt quite work right
        elif sMenuChoice == 4:
            bFullGameQuit = True
            return 