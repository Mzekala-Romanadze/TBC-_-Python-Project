# This program gets and prints information about friendships between people.
# If the program gets 'FINISH' it ends working.
# if the user enters Nini - Demetre, it means that Nini is a friend of Demetre's and vice versa.
# Example #1
# Input:
#       Demetre – Elene
#       Mariam – Tornike
#       Demetre – Tornike
#       FINISH
# Output:
#       Demetre - Elene, Tornike
#       Elene - Demetre
#       Mariam - Tornike
#       Tornike - Mariam, Demetre


def get_friendships():
    friendships = {}
    while True:
        user_input = input("Enter names of 2 people in format: 'Name 1 - Name 2' or 'FINISH' to end: ").split()
        if user_input[0].upper() == 'FINISH':
            break
        if len(user_input) != 3:
            print("Please, enter names in format: 'Name 1 - Name 2'")
            continue

        name_1, name_2 = user_input[0], user_input[2]

        if name_1 not in friendships:
            friendships[name_1] = [name_2]
        else:
            friendships[name_1].append(name_2)

        if name_2 not in friendships:
            friendships[name_2] = [name_1]
        else:
            friendships[name_2].append(name_1)

    return friendships


def main():
    friendships = get_friendships()

    print("The friendship result: ")
    for key, value in friendships.items():
        print(f"{key} - {value}")


if __name__ == "__main__":
    main()
