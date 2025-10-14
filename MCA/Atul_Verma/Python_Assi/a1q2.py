# Q2 Find the probability of rolling a dice / flipping a coin (using functions)

def probability_dice(roll, sides=6):
    if roll < 1 or roll > sides:
        return 0
    return 1 / sides

def probability_coin(side):
    if side.lower() in ['heads', 'tails']:
        return 1 / 2
    else:
        return 0

# Examples
print("Probability of rolling a 4 on a dice:", format(probability_dice(4),".2f"))
print("Probability of getting heads on a coin:", probability_coin('heads'))
