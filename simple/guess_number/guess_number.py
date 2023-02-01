import random

def guess(x):
    random_number = random.randint(1, x)
    feedback = ''

    while feedback != 'c':
        try:
            user_input = int(input(f"Guess the number in a range of [1, {x}]\n"))
            if user_input > x or user_input < 1:
                raise TypeError("ERROR: Input is incorrect, it should be less than 21 or higher than 0")
            if user_input > random_number:
                print(f"{user_input} is too high")
            elif user_input < random_number:
                print(f"{user_input} is too low")
            else:
                feedback = 'c'
                print(f"{user_input} is correct")
        except TypeError as error:
            print(f"{error}")
        except ValueError:
            print("ERROR: Input is incorrect, it should be an integer")

def computer_guess(x):
    highest_number = x
    lowest_number = 1
    attempts = 0

    feedback = ''

    while feedback != 'c':
        try:
            random_number = random.randint(lowest_number, highest_number)
            user_input = input(f"Number {random_number} is (H) too high, (L) lower or (C) correct?\n").upper()
            if user_input not in ('H', 'L', 'C'):
                raise ValueError("Only H, L and C is allowed as input")
            if user_input == "H":
                attempts += 1
                highest_number = random_number - 1
                print(highest_number)
            elif user_input == "L":
                attempts += 1
                lowest_number = random_number + 1
            elif user_input == "C":
                feedback = 'c'
                print(f"You found the number in {attempts} attempts")
        except TypeError as error:
            print(f"{error}")
        except ValueError as error:
            print(f"{error}")

# guess(20)
computer_guess(200)