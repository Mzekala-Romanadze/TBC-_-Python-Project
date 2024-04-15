import random


def generate_random_choice():
    random_choice = random.choice(["R", "P", "S"])
    return random_choice


def main():
    user_choice = input("Enter your choice: rock(R), paper(P), scissor(S) ")
    random_choice = generate_random_choice()
    if user_choice != "R" or user_choice != "P" or user_choice != "S":
        print("Wrong choice. please enter valid card.")
        exit()
    if user_choice == random_choice:
        print("It is tie.")
    elif user_choice == "R" and random_choice == "S":
        print("You are winner.")
    elif user_choice == "S" and random_choice == "P":
        print("You are winner.")
    elif user_choice == "P" and random_choice == "R":
        print("You are winner.")
    else:
        print("Game is over. The computer is winner.")


if __name__ == "__main__":
    main()
