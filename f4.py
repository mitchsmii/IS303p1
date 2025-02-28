import random

def simulate_game():
    wins = 0
    losses = 0
    
    hScore = random.randint(0, 9)
    aScore = random.randint(0, 9)
    
    for iCount in range(random.randint(0, 9)) :
        while hScore == aScore:
            hScore = random.randint(0, 9)
            aScore = random.randint(0, 9)
        
        if hScore > aScore:
            wins += 1
        else:
            losses += 1
    
    return wins, losses
