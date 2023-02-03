import random

def play():
    exit_game = 0
    while exit_game != 1:
        try:
            user_input = input("Choose (R) for rock, (P) for paper, (S) for scissors or (Q) to exit the game\n").upper()
            computer_choice = random.choice(['R', 'P', 'S'])

            if user_input not in ('R', 'P', 'S', 'Q'):
                raise ValueError('Only R, S, P and Q are allowed as input')
            if user_input == 'Q':
                exit_game = 1
            if is_win(user_input, computer_choice) == 'Win':
                print(f"WIN: You ({user_input}) vs Computer ({computer_choice})\n")
            elif is_win(user_input, computer_choice) == 'Lose':
                print(f"LOSE: You ({user_input}) vs Computer ({computer_choice})\n")
            elif is_win(user_input, computer_choice) == 'Tie':
                print(f"TIE: You ({user_input}) vs Computer ({computer_choice})\n")
        except ValueError as error:
            print(f"{error}")
        except TypeError as error:
            print(f"{error}")

def is_win(user_input, computer_choice):
    if user_input == 'R':
        if computer_choice == 'R':
            return 'Tie'
        elif computer_choice == 'S':
            return 'Win'
        else:
            return 'Lose'
    if user_input == 'S':
        if computer_choice == 'R':
            return 'Lose'
        elif computer_choice == 'S':
            return 'Tie'
        else:
            return 'Win'
    if user_input == 'P':
        if computer_choice == 'R':
            return 'Win'
        elif computer_choice == 'S':
            return 'Lose'
        else:
            return 'Tie'

play()