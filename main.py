# main page that will call the other functons


# imports f1 (dispalyGameIntro) and the global variable sUserName
from displayGameIntro import displayGameIntro
from f2 import Menu
from f3 import fullGame
from f4 import simulate_game


playAgain = True

while playAgain == True :
    # calls displayGameIntro (Function 1) to display game into and return sUserName
    sUserName = displayGameIntro()

    # show menu and show what option user chose
    sMenuChoice = int(Menu())
    print(sMenuChoice)

    if sMenuChoice == 4 :
        playAgain = False
    else :
        sHomeTeam, sAwayTeam = fullGame(sMenuChoice)

        # simulate_game(sHomeTeam, sAwayTeam)

        iWins, iLosses = simulate_game()

        print(f'\n{sHomeTeam}: Wins: {iWins} Losses: {iLosses}') 

        userInput = input("Do you want to play again? (y/n) ")
        if userInput == "y" :
            playAgain = True
        else :
            playAgain = False

print("Ok Goodbye!")
    
