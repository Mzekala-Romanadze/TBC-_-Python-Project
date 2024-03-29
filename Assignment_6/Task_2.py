# This program checks the password is either correct or not.
# The password is defined in advance as the constant and the user
# have to guess it to get access. The user has 3 tries.
# You can change the MAX_TRIES number and the program still works.

REAL_PASSWORD = "SkyLight"
MAX_TRIES = 3

password = input("Please enter password: (You have 3 tries) ")

for i in range(1, MAX_TRIES + 1):
    if REAL_PASSWORD != password:
        if i == MAX_TRIES:
            print("You are blocked!")
            break
        password = input("Password is not correct. Try again ")
    if REAL_PASSWORD == password:
        print("It is a correct password. Now, you can see the sky")
        break
