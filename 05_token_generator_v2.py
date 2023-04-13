"""
Component 3 (random tokens) v2
Calculates user balance based on random selection of tokens
"""

import random

tokens = ["unicorn", "horse", "donkey", "zebra"]
balance = 100

# Testing loop to generate 20 tokens
for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t')  # can crop output making it easier to screenshot


    # adjust balance
    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= 0.50

    # Output
    print(f"Token: {token}, Balance: ${balance}")