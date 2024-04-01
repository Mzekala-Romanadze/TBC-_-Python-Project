# This program gets a positive integer n
# and finds the divisors of all numbers until n (only first 3 divisors).

number = int(input("What is n? "))


def get_divisors():
    for i in range(1, number + 1):
        divisors = []
        for j in range(1, number + 1):
            if i % j == 0:
                divisors.append(j)
                if len(divisors) > 2:
                    break
        print(f"Divisors of {i}: are {divisors}")


if 0 < number < 50:
    get_divisors()
else:
    print("Enter a positive integer in range 0-50")
