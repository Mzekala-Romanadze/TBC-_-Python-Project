# This program gets a positive integer n in range 0-20
# and finds all terms in a sequence from 0 to n.
# The null term is 0 and the first term is 1.
# In the sequence each next term is the sum of the previous two terms.
# While loop is used to solve the problem (List should not be used).

n = int(input("Enter a positive integer in range 0-20: "))

if 0 <= n < 20:
    null_member = 0
    first_member = 1
    print("The terms in a sequence from 0 to", n, "are: ")
    print(null_member, end=" ")
    while n > 1:
        print(first_member, end=" ")
        null_member, first_member = first_member, null_member + first_member
        n -= 1
else:
    print("Please, enter a positive integer in range 0-20")
