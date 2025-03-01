import random

def simulate_game():
    wins = 0
    losses = 0
    
    iHomeScore = random.randint(0, 9)
    iAwayScore = random.randint(0, 9)
    
    for iCount in range(random.randint(1, 11)) :
        while iHomeScore == iAwayScore:
            iHomeScore = random.randint(0, 11)
            iAwayScore = random.randint(0, 11)
        
        if iHomeScore > iAwayScore:
            wins += 1
        else:
            losses += 1
    
    return wins, losses
