def Menu():
    count = 1

    # Makes sure that the value entered is in range of the menu
    while count != 0:
        try:
        
            # Prints menu
            sMenuChoice = int(input("""
                    Menu               
            1. Choose your team
            2. Choose opponent team
            3. Show rules again
            4. Play again
            5. Quit         
                
        Which option would you like to choose? """))
        
            if sMenuChoice in range(1, 6):
                count = 0

        except ValueError:
            print("Please choose a valid menu option")
    
    return sMenuChoice

Menu()
#quit
#play again
#choose your team
#choose opponent team
#show rules again 