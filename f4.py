import random

wins = 0
losses = 0

# Randomly generate scores for both the home and away teams.
hScore = random.randint(0, 9)
aScore = random.randint(0, 9)
# If the scores are equal (a tie), keep generating new scores until there is a clear winner.
while hScore == aScore:
    hScore = random.randint(0, 9)
    aScore = random.randint(0, 9)
# Determine if the home team won (W) or lost (L) based on the final scores.
if hScore > aScore:
    gameResult = "W"
    wins += 1
else:
    gameResult = "L"
    losses += 1