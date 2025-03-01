# main page that will call the other functons


# imports f1 (dispalyGameIntro) and the global variable sUserName
from displayGameIntro import displayGameIntro
from f2 import Menu
from f3 import fullGame
from f4 import simulate_game


playAgain = True

while playAgain == True :
    # calls displayGameIntro (Function 1) to display game info and return sUserName
    sUserName = displayGameIntro()

    # show menu and show what option user chose
    sMenuChoice = int(Menu())
    print(f'\nYou selected option {sMenuChoice}.')

    if sMenuChoice == 4 :
        playAgain = False
    else :
        sHomeTeam, sAwayTeam = fullGame(sMenuChoice)

        # simulate_game(sHomeTeam, sAwayTeam)

        iWins, iLosses = simulate_game()

        print(f'\n{sHomeTeam} vs. {sAwayTeam}: \nWins: {iWins} Losses: {iLosses}') 

        # initialized exception handling to only allow y or n to be inputted. 
        bContinue = True

        while bContinue:
            userInput = input("Do you want to play again? (y/n) ").strip().lower()
            
            if userInput == "y":
                playAgain = True
                bContinue = False  # Exit loop
            elif userInput == "n":
                playAgain = False
                bContinue = False  # Exit loop
            else:
                print("\nInvalid input. Please enter 'y' or 'n'.\n")

print("\nGoodbye!")
    
