"""
Component 3 (random tokens) v4
Calculate percentages to ensure the odds favour the house
5% unicorns, 30% donkeys, and the remaining 65% horses/zebras
"""

import random

tokens = ["unicorn", "donkey", "horse", "zebra"]
STARTING_BALANCE = 100
balance = STARTING_BALANCE

# Testing loop to generate 100 tokens
for percentage in range(10):
    percent = random.randint(1, 100)

    # token type
    # if the percentage is lower than or equal to 5
    # user gets a unicorn
    if percent <= 5:
        token = tokens[0]

    # if the percentage is larger than 5 and lower than or equal to 35
    # user gets a donkey
    elif 5 < percent <= 35:
        token = tokens[1]

    # in all other cases the token must be a horse or zebra
    # if the percentage is even, user gets a horse
    elif percent % 2 == 0:
        token = tokens[2]

    # if the percentage is odd, user gets a zebra
    else:
        token = tokens[3]

    # adjust balance
    # if token is a unicorn, add $4 to balance
    if token == "unicorn":
        balance += 4

    # if token is a donkey, subtract $1 from balance
    elif token == "donkey":
        balance -= 1

    # otherwise (horse/zebra) subtract $0.50 from balance
    else:
        balance -= 0.50

    # Output
    print(f"Token: {token} Balance: {balance:.2f}")

print()
print(f"Starting balance: ${STARTING_BALANCE:.2f}")
print(f"Final balance: ${balance:.2f}")