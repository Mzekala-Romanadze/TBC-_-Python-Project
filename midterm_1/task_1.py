# Task_1: (5 ქულა) Დაწერეთ პროგრამა რომელიც მომხმარებელს მოსთხოვს
# შეიყვანოს შემდეგი მონაცემები: სახელი, გვარი და ასაკი.
# Ეს ინფორმაცია Პროგრამამ ეკრენზე უნდა დაბეჭდოს შემდეგ ფორმატში:
# Hello სახელი გვარი.
# Age: ასაკი.


def main():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    age = input("Enter age: ")

    if not age.isnumeric():
        print("Please, enter correct age.")
        exit(1)
    print(f"Hello {name} {surname}.")
    print(f"Age: {age}.")


if __name__ == "__main__":
    main()
