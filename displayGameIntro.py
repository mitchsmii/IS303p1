# Justin Maxwell - 2/24/2025 

# Display an introduction to the game explaining rules and 
# prompt for their name and display that in the welcome message. 
# Return the name to the main program and store it in variable 
# so it can be used throughout the program.

# imports textwrap to remove the indent from the paragraph
import textwrap

# Function 1: Displays game intro, prompts user for name, displays welcome message
def displayGameIntro() :

    # Game intro text with textwrap.dedent to remove the indent (because it's in the function, it has an indent for some reason)
    sIntroParagraph = textwrap.dedent("""
    Welcome to the game.

    A list of teams will be displayed:
    - You will choose the home team 
    - Then you will choose the away team 

    Then the final record and game data for the home team will be displayed.
    """)

    #prints the intro paragraph
    print(sIntroParagraph)


    # prompts the user for their name and stores it in the sUserName variable
    # input cannont be empty
    bContinue = True
    while bContinue :
        sUserInput = input("Please enter your name: ")
        if sUserInput.strip() == "" :
            print("\nInput cannot be empty. Please enter your name:\n")
            continue
        try : 
            sUserName = sUserInput
            bContinue = False
        finally :
            bContinue = False


    # display a welcome message with the sUserName
    print(f"\nWelcome to the game {sUserName}. Let's get started, shall we?\n")
    return sUserName