# This program gets a positive integer n from the user
# and paints the Christmas tree which has n height.

n = int(input("Enter Christmas tree height: "))


def get_tree():
    for i in range(1, n):
        left = "/" * i
        right = "\\" * i
        space = (" " * (n - i))
        result = space + left + "|" + right
        print(result)


if 0 < n < 50:
    star = (" " * n) + "*"
    print(star)
    get_tree()
    trunk = (" " * n) + "|"
    print(trunk)
else:
    print("Enter a positive integer in range 0-50")
