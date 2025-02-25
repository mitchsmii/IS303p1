#Carson Hendrix 2/25/2025

#This code will make the menu and then allow
#the user to choose which menu choice they want
#then return the choice that they choice for the menu


def Menu():
    count = 1

    # Makes sure that the value entered is in range of the menu
    while count != 0:

        # Make sure that the user enters a number
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
        
            # end the loop if user input is within 1-5
            if sMenuChoice in range(1, 6):
                count = 0

        except ValueError:
            print("Please choose a valid menu option")
    
    return sMenuChoice

Menu()