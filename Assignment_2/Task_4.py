# This program gets the speed of the car from the user
# and prints the category of the speed on the screen.
# If the car speed covers more than 1 category the faster category should be chosen.

speed = int(input("What's the speed of the car? "))
SLOW = speed < 30
MODERATE = 30 < speed < 60
FAST = 60 < speed < 120
VERY_FAST = 120 < speed

if speed <= 0:
    print("Enter number more than 0")
elif SLOW:
    print("Car's speed category is Slow.")
elif MODERATE:
    print("Car's speed category is Moderate.")
elif FAST:
    print("Car's speed category is Fast.")
else:
    print("Car's speed category is Very fast.")
