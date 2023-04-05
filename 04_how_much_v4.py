"""
Component 2 (How much) v3
More efficient method - includes valid range as the basis of the while loop
which eliminates the need to use the 'valid' variable
"""


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


# Main routine
user_balance = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${user_balance}")