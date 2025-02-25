# Justin Maxwell - Prof. Anderson - Assignment 4
# Stores information about Wins and Losses for Women's soccer

# Asks about a home women's soccer team
# and how many games they played
# then display the scores of each game
# as well as the overall record of the home team for the season

# LASTLY display all the information stored in the dictionary
# IN THE DICTIONARY store your team name, your team score
# the opponent team name, the opponent team score, and if it was W or L

# imports random for RNG
import random

# creates the main dictionary
soccerGamesDict = {}

# declares win/loss count variables
iWinCount = 0
iLossCount = 0

# Inputs the home team's name -- cannot enter empty value
bContinue = True
while bContinue :
    userInput = input("What if your home team's name? ")
    if userInput.strip() == "" :
        print("\nInput cannot be empty. Please enter your team's name.\n")
        continue
    try :
        sHomeTeamName = userInput
        bContinue = False
    finally : 
        bContinue = False

#  inputs how many games they played -- has to enter a whole number
bContinue = True
while bContinue == True :
    try :
        iNumGames = int(input(f"How many games did {sHomeTeamName} play this season? (enter whole number) "))
        bContinue = False
    except ValueError :
        print("\nInvalid input. Please enter a whole number.\n")
  

# for loop that goes through the number of games and inputs info into a new dictionary
for iCount in range(0, iNumGames) :
        
    # Inputs the name of the away team -- making sure they don't input empty values
    bContinue = True
    while bContinue :
        userInput = input(f"Enter the name of the away team for Game {iCount + 1}: ")
        if userInput.strip() == "" :
            print("\nInput cannot be empty. Please enter the team's name.\n")
            continue
        try :
            sAwayTeamName = userInput
            bContinue = False
        finally : 
            bContinue = False
    
    # makes sure their input isn't empty -- inputs the state the game was played in
    bContinue = True
    while bContinue :
        userInput = input("What state was that game played in? ")
        if userInput.strip() == "" :
            print("\nInput cannot be empty. Please enter the state the game was played in.\n")
            continue
        try :
            sGameState = userInput
            bContinue = False
        finally : 
            bContinue = False

    # makes random scores
    iHomeScore = random.randrange(0, 5)
    iAwayScore = random.choice([0,1,2,3,4,5])

    # loop to generate W and L if score is == to not generate ties
    while iHomeScore == iAwayScore :
        iHomeScore = random.randrange(0, 5)
        iAwayScore = random.choice([0,1,2,3,4,5])

    # if/else to determine W/L 
    if iHomeScore > iAwayScore :
        sHomeWL = "W"
        iWinCount += 1 # stores # of wins
    else :
        sHomeWL = "L"
        iLossCount += 1 # stores # of losses

    # adds data to sub-dictionary
    key = f'Game {iCount + 1}'
    soccerGamesDict[key] = {
        'homeName': sHomeTeamName,
        'awayName': sAwayTeamName,
        'state': sGameState,
        'homeScore': iHomeScore,
        'awayScore': iAwayScore,
        'W/L': sHomeWL,
    }

print("\nScores from the season:\n")

# prints the final season record, iterating through however many Games were added
for iCount in range(0, iNumGames) :
    key = f'Game {iCount + 1}' # uses same code to find the game as was to create the key name 

    # assigns variables now to values found in each dictionary
    sHomeName = soccerGamesDict[key]['homeName']
    iHomeScore = soccerGamesDict[key]['homeScore']
    sAwayName = soccerGamesDict[key]['awayName']
    iAwayScore = soccerGamesDict[key]['awayScore']

    #prints the names and scores
    print(f"{sHomeName}'s score: {iHomeScore} {sAwayName}'s score: {iAwayScore} ")

# prints Home Team's final record
print(f'\nFinal season record: {iWinCount} - {iLossCount}')

# creates variable with W/L record to use soon
fWLRatio = (iWinCount/(iWinCount + iLossCount))

# uses fWLRatio to determine how good the team did
if fWLRatio >= .75 :
    print("\nQualified for the NCAA Women's Soccer Tournament!\n")
elif fWLRatio >= .5 :
    print("\nYou had a good season.\n")
else :
    print("\nYour team needs to practice.\n")


# Turn all into functions to imrove flow and readiblity
# then SEE BELOW


# THEN create code where they can ask for data on a certain game
# "input(What game? ) = enters 1-5 (depending on how many games were played)"
# use the inputted number and combine it with "Game" to search for the key
# then it prints the data for that game