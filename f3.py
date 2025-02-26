#3. Display list of all teams and allow the user to choose a team using a menu. 
# Call the function again to let the user choose the opponent but do not display 
# the team they chose previously. Remove that team from the list. Allow the user 
# to select an opponent, and return team name. This function should receive a 
# parameter but give it a default value if none is passed. You can use this 
# function for both choosing the home team and the opponent team.

from f2 import Menu
from displayGameIntro import displayGameIntro

def fullGame(sMenuChoice):

    # All teams
    BYU = "BYU"
    UVU = "UVU"
    SUU = "SUU"
    utahState = "Utah State"
    universityOfUtah = "University of Utah"

    teamList = [BYU, UVU, SUU, utahState, universityOfUtah]
    
    count = 1

    #loop until they want to get out of this menu
    while count != 0:
        if sMenuChoice == 1:

        # Choose home team
            secondCount = 1
            while secondCount != 0 :
                try :
                    iHomeTeam = int(input(f"Choose your team:\n 1. {BYU}\n 2. {UVU}\n 3. {SUU}\n 4. {utahState}\n 5. {universityOfUtah}\n Who do you want your home team to be? (Enter a number 1-5) "))

                    if iHomeTeam in range(1, 6) :
                        secondCount = 0
                    else :
                        print("Please enter a number between 1-5.\n")

                except ValueError :
                    print("\nPlease choose a number between 1-5.\n")


            # iHomeTeam = int(input(f"Choose your team:\n 1. {BYU}\n 2. {UVU}\n 3. {SUU}\n 4. {utahState}\n 5. {universityOfUtah}\n Who do you want your home team to be? (Enter a number 1-5) "))
            teamList.pop(iHomeTeam - 1)
            sMenuChoice = Menu()

        elif sMenuChoice == 2:

        # Choose opponents team
            print("Choose opponent team:")
            count = 0
            for i in range(1, 5):
                print(f"{count + 1}. {teamList[count]}\t")
                count += 1
            iOppTeam = input("Who do you want your opponents team to be? (Enter a number 1-4)")

            # THEY CAN ONLY LEAVE THE LOOP IF THEY QUIT OR CHOOSE THEIR TEAM AND OPP TEAM
            return iHomeTeam
            return iOppTeam
        
        elif sMenuChoice == 3:

        #show rules again
            displayGameIntro()
            sMenuChoice = Menu()

        #im pretty sure that this part doesnt quite work right
        elif sMenuChoice == 4:
            print("Play again")
            fullGame()

        #quit the loop
        elif sMenuChoice == 5:
            print("quit")
            count = 0