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
    if percent <= 5:
        token = tokens[0]
    elif 5 < percent <= 35:
        token = tokens[1]
    elif percent % 2 == 0:
        token = tokens[2]
    else:
        token = tokens[3]


    # adjust balance
    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= 0.50

    # Output
    print(f"Token: {token} Balance: {balance:.2f}")

print()
print(f"Starting balance: ${STARTING_BALANCE:.2f}")
print(f"Final balance: ${balance:.2f}")