# Midterm task 3: Game _ Rock, Paper, Scissor (play up to 3 points)

import random

OPTION_SET = "RPS"


def get_random_choice():
    i = random.randint(0, 2)
    return OPTION_SET[i]


def game_rules(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw."
    elif computer_choice == "R" and user_choice == "S":
        winner = "Computer"
    elif computer_choice == "S" and user_choice == "P":
        winner = "Computer"
    elif computer_choice == "P" and user_choice == "R":
        winner = "Computer"
    else:
        winner = "User"
    return winner


def main():
    user_score = 0
    computer_score = 0
    game_round = 0
    while user_score < 3 and computer_score < 3:
        user_choice = input("Enter your choice: [rock(R), paper(P), scissor(S)] ").upper()

        if user_choice not in OPTION_SET:
            print("Wrong choice. Enter a valid choice.")
            continue

        computer_choice = get_random_choice()
        winner = game_rules(user_choice, computer_choice)

        print(f"User's choice: {user_choice}.")
        print(f"Computer's choice: {computer_choice}.")
        print(f"Round Winner: {winner}")

        if winner == "User":
            game_round += 1
            user_score += 1
        elif winner == "Computer":
            game_round += 1
            computer_score += 1
        else:
            game_round += 1

    print(f"User's Score: {user_score}")
    print(f"Computer's Score: {computer_score}")
    print("Number of rounds:", game_round)

    if user_score > computer_score:
        print("Congratulations! You win the game!")
    else:
        print("Game over. Computer wins the game!")


if __name__ == "__main__":
    main()
