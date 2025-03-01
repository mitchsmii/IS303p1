#Carson Hendrix 2/25/2025
#Edited by Joseph Xiong

#This code will make the menu and then allow
#the user to choose which menu choice they want
#then return the choice that they choice for the menu

# imports textwrap to remove the indent from the paragraph
import textwrap

def Menu():
    menuQuit = False

    # Makes sure that the value entered is in range of the menu
    while menuQuit == False:

        # Make sure that the user enters a number
        try:
        
            # Prints menu and removes the indent
            sMenuText = textwrap.dedent("""
            Menu
            1. Choose your team
            2. Choose opponent team
            3. Show rules again
            4. Quit 
            """)

            print(sMenuText)            
            sMenuChoice = int(input("Which option would you like to choose? (enter number 1-4) "))
        
            # end the loop if user input is within 1-4
            if sMenuChoice in range(1, 5):
                menuQuit = True
            else: 
                print('Please enter a valid menu option.')

        except ValueError:
            print("\nPlease choose a valid menu option.")
    
    return sMenuChoice