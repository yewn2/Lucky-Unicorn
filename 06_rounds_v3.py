"""
Component 4 - game mechanics and looping v3
Converting v2 into a function
"""

import random


# function to generate random token
def generate_token(balance):
    tokens = ["unicorn", "donkey", "horse", "zebra"]
    rounds_played = 0
    play_again = ""

    # Testing loop to generate tokens
    while play_again != "x":
        rounds_played += 1  # keep track of rounds
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
        print()
        print(f"Round: {rounds_played} Token: {token} Balance: {balance:.2f}")
        print()

        if balance > 0:
            # does user want to play again
            play_again = input("Do you want to play another round?\n"
                               "<enter> to play again or 'x' to exit ")
        else:
            print("Sorry, you have run out of money")
            print()
            break
    return balance


# main routine
starting_balance = 5
closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You started with ${starting_balance:.2f}\n"
      f"and leave with ${closing_balance:.2f}")
print("Goodbye")
