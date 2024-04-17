# This program gets two integers a and b from the user.
# 0 < a, b < 10000. The program prints the GCD (Greatest Common Divisor)
# of a and b.
# The problem is solved by using two methods: Iterative and Recursive.


def iter_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def rec_gcd(a, b):
    if b == 0:
        return a
    return rec_gcd(b, a % b)


def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    if 0 < a <= 10000 and 0 < b <= 10000:
        print(f"Using iterative method, GCD of {a} and {b} is: {iter_gcd(a, b)}")
        print(f"Using recursive method, GCD of {a} and {b} is: {rec_gcd(a, b)}")
    else:
        print("Wrong number(s). Enter value as an integer of a and b in range 0-10000.")


if __name__ == "__main__":
    main()
