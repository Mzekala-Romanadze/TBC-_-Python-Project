# This program gets a positive integer from the user
# and calculates the nth term in the sequence where the first term is 1,
# the null term is 0 and each next term is the sum
# of the previous two terms.


def get_integer():
    while True:
        try:
            number = int(input("Enter a positive integer: "))
            if 0 <= number < 20:
                return number
            else:
                print("Enter a positive integer from 1 to 20.")
        except ValueError:
            print("Enter a positive integer from 1 to 20.")


def nth_term():
    prev_term1, prev_term2 = 1, 0
    current_term = []
    for _ in range(2, n + 1):
        current_term = prev_term1 + prev_term2
        prev_term2 = prev_term1
        prev_term1 = current_term
    return current_term


n = get_integer()
term = nth_term()
if n == 0:
    print("The 0th term in the sequence is 0.")
elif n == 1:
    print("The 1st term in the sequence is 1.")
else:
    print(f"The {n}th term in the sequence is: {term}")
