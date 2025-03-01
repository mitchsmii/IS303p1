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

        count = 0
        while count != 1:
            userInput = input("Do you want to play again? (y/n) \n")
            if userInput == "y" :
                playAgain = True
                count = 1
            elif userInput == "n":
                playAgain = False
                count = 1
            else:
                print("Please enter a valid input.")

print("Goodbye!")
    
