# This program gets two integers a and b from the user.
# 0 < a, b < 10000. The program prints the least common multiple (LCM)
# of a and b. LCM(a,b) = (a*b)/gcd(a,b)
# The problem is solved by using two methods: Iterative and Recursive.

from Task_1 import iter_gcd
from Task_1 import rec_gcd


def iter_lcm(a, b):
    return (a * b) // iter_gcd(a, b)


def rec_lcm(a, b):
    return (a * b) // rec_gcd(a, b)


def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    if 0 < a <= 10000 and 0 < b <= 10000:
        print(f"Using iterative method, LCM of {a} and {b} is: {iter_lcm(a, b)}")
        print(f"Using recursive method, LCM of {a} and {b} is: {rec_lcm(a, b)}")
    else:
        print("Wrong number(s). Enter value as an integer of a and b in range 0-10000.")


if __name__ == "__main__":
    main()
