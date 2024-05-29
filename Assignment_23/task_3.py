# This program extends the standard library's data structure list - using inheritance.
# ExtendedList class has two methods added: min and max
# which returns the minimum and maximum numbers from the list.

class ExtendedList(list):
    def min(self):
        if not self:
            return ValueError("Does not exist. The list is empty")
        else:
            return min(self)

    def max(self):
        if not self:
            return ValueError("Does not exist. The list is empty")
        else:
            return max(self)


def main():
    list_1 = ExtendedList([6, 12, 24, 30, 36])
    list_2 = ExtendedList([60, 20, 30, 80, -120])
    list_3 = ExtendedList([-5, 0, 5, 10, 15])
    list_4 = ExtendedList([])

    print(f"List_1: {list_1}")
    print(f"Minimum number from list_1: {list_1.min()}")
    print(f"Maximum number from list_1: {list_1.max()}")

    print(f"List_2: {list_2}")
    print(f"Minimum number from list_2: {list_2.min()}")
    print(f"Maximum number from list_2: {list_2.max()}")

    print(f"List_3: {list_3}")
    print(f"Minimum number from list_3: {list_3.min()}")
    print(f"Maximum number from list_3: {list_3.max()}")

    print(f"List_4: {list_4}")
    print(f"Minimum number from list_4: {list_4.min()}")
    print(f"Maximum number from list_4: {list_4.max()}")


if __name__ == '__main__':
    main()
