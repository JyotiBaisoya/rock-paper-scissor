import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()
        if user_choice in ['rock', 'paper', 'scissors', 'q']:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def play_game():
    user_wins = 0
    computer_wins = 0
    draws = 0

    while True:
        print("Rock, Paper, Scissors")
        print("---------------------")
        print(f"User wins: {user_wins}\tComputer wins: {computer_wins}\tDraws: {draws}\n")

        user_choice = get_user_choice()
        if user_choice == 'q':
            break

        computer_choice = get_computer_choice()

        print(f"\nUser's choice: {user_choice.capitalize()}")
        print(f"Computer's choice: {computer_choice.capitalize()}\n")

        winner = determine_winner(user_choice, computer_choice)
        if winner == 'draw':
            print("It's a draw!\n")
            draws += 1
        elif winner == 'user':
            print("You win!\n")
            user_wins += 1
        else:
            print("Computer wins!\n")
            computer_wins += 1

    print("Final Score:")
    print(f"User wins: {user_wins}\tComputer wins: {computer_wins}\tDraws: {draws}\n")
    print("Thanks for playing!")

play_game()
