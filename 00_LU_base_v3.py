"""
LU base component v1
Components added after they have been created and tested
"""
import random


# yes/no checking function
def yes_no(question_text):
    while True:
        # Ask the user if they have played before
        answer = str(input(question_text)).strip().lower()

        # If they say yes,  output 'Program Continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no , output 'Display Instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print(" please input yes or no")


# function to display instructions
def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the game will go here")
    print()


# function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# number checking function
def num_check(question, low, high):
    error = ("That was not a valid input\n"
             "Please enter a valid number between {} and {}\n".format(low, high))

    # Keep asking until a valid amount (1-10) is entered
    while True:
        try:
            # ask for amount
            response = int(input(question))

            # check for number within the required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


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
            print(formatter("!", "Congratulations, you got a unicorn"))
            print()

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


# Main routine goes here:
print(formatter("-", "Welcome to the Lucky Unicorn Game"))
print()
played_before = yes_no("Have you played this game before?")

if played_before == "No":
    instructions()


# ask the user how much they want to play with
starting_balance = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${starting_balance}")

closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You started with ${starting_balance:.2f}\n"
      f"and leave with ${closing_balance:.2f}")
print()
print(formatter("*", "Goodbye"))