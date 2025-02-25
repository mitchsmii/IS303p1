import random

def simulate_game():
    wins = 0
    losses = 0
    
    hScore = random.randint(0, 9)
    aScore = random.randint(0, 9)
    
    while hScore == aScore:
        hScore = random.randint(0, 9)
        aScore = random.randint(0, 9)
    
    if hScore > aScore:
        gameResult = "W"
        wins += 1
    else:
        gameResult = "L"
        losses += 1
    
    return gameResult, wins, losses
