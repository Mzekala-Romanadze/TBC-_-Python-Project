# This program gets a positive integer n in range 0-20 from the user
# and finds the nth term in the sequence where the first term is 1,
# the null term is 0 and each next term is the sum
# of the previous two terms.

n = int(input("Enter a positive integer in range 0-20: "))

if 0 <= n < 20:
    if n == 0:
        print("The 0th term is: ", 0)
    else:
        zero_term = 0
        first_term = 1
        current_term = 1
        for i in range(1, n):
            current_term = zero_term + first_term
            zero_term = first_term
            first_term = current_term
        print(f"The {n}th term is: ", current_term)
else:
    print("Enter a positive integer in range 0-20.")
