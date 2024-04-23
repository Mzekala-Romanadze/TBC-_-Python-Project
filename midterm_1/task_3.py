# Task_3: (12 ქულა) Დაწერეთ თამაში rock, paper, scissor.
# Დაწერეთ ფუნქცია რომელიც დააგენერირებს შემთხვევითად ერთ-ერთ სიმბოლოს
# ჩამოთვლილი სამიდან R,P,S. Დაწერეთ მეორე ფუნქცია main, რომელშიც
# მომხმარებელს შეაყვანინებთ თავის არჩევანს R, P ან S. სიმარტივისთვის შეგიძლიათ
# უგულებელყოთ ყველა შემოწმება მომხმარებლის ინფუთზე. Შეადარეთ
# ერთმანეთს მომხმარებლის შემოყვანილი სიმბოლო და თქვენი ფუნქციის დაგენერირებული სიმბოლო
# და გამოავლინეთ გამარჯვებული.
# Წესები: R ამარცხებს S; S ამარცხებს P; P ამარცხებს R; P P, R R, S S არის ფრე.

import random

OPTION_SET = "RPS"


def get_random_choice():
    i = random.randint(0, 2)
    return OPTION_SET[i]


def game_rules(user_choice, computer_choice):
    winner = "Winner is "
    if user_choice == computer_choice:
        return "It's draw."
    elif computer_choice == "R" and user_choice == "S":
        winner += "Computer"
    elif computer_choice == "S" and user_choice == "P":
        winner += "Computer"
    elif computer_choice == "P" and user_choice == "R":
        winner += "Computer"
    else:
        winner += "User"

    return winner


def main():
    user_choice = input("Enter your choice: [rock(R), paper(P), scissor(S)] ").upper()
    if user_choice not in OPTION_SET:
        print("Wrong choice. Enter valid choice.")
        return None

    computer_choice = get_random_choice()
    winner = game_rules(user_choice, computer_choice)

    print(f"User's choice: {user_choice}.")
    print(f"Computer's choice: {computer_choice}.")
    print(winner)


if __name__ == "__main__":
    main()
