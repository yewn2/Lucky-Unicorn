"""
Component 3 (random tokens) v3
Calculates user balance based on random selection of tokens
"""

import random

tokens = ["unicorn",
          "horse", "horse", "horse",
          "donkey", "donkey", "donkey",
          "zebra", "zebra", "zebra"]
STARTING_BALANCE = 100
balance = STARTING_BALANCE

# Testing loop to generate 100 tokens
for item in range(500):
    token = random.choice(tokens)


    # adjust balance
    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= 0.50

    # Output
print(f"Starting balance: ${STARTING_BALANCE:.2f}")
print(f"Final balance: ${balance:.2f}")