# This program gets a positive integer n (n > 1) from the user
# and calculates x. x is calculated in accordance with
# the following formula: x = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ... (+/-)1 / (2n-1) )

n = int(input("Enter positive integer (n > 1): "))

if n > 1:
    x = 0
    k = 1  # For changing the sign of the number
    for i in range(1, n + 1):
        x += k * (1 / (2 * i - 1))
        k *= -1
    x *= 4
    print(f"When the input number is {n}, the 'x' equals: ", x)
else:
    print("Incorrect number. Please, Enter positive number (n > 1).")

# Answer to the question: The program allows us to observe
# how the value of x converges as n increases, in particular,
# providing increasingly accurate approximations of x as n grows larger.
