# This program has a class Inset and in the constructor an empty list is created.
# The Inset class has the following methods:
#           1. Insert - which adds unique elements to the list.
#           2. Member - which checks if the element is in the list -
#              returns True if it is, and False if it is not.
#           3. Remove - removes an element from the list -
#              if an element is not found in the list, it raises a ValueError with the message "Not found"
# The Inset class has a __str__ that first sorts the list in ascending order
# and then returns its elements as a string.

class Inset:
    def __init__(self):
        self.unique_elements = []

    def insert(self, element):
        if element not in self.unique_elements:
            self.unique_elements.append(element)

    def member(self, element):
        if element in self.unique_elements:
            return True
        return False

    def remove(self, element):
        if element in self.unique_elements:
            self.unique_elements.remove(element)
        else:
            print("Not found")

    def __str__(self):
        sorted_elements = sorted(self.unique_elements)
        return str(sorted_elements)


def main():
    inset = Inset()

    inset.insert(30)
    inset.insert(80)
    inset.insert(60)
    inset.insert(30)
    inset.insert(15)
    inset.insert(88)
    inset.insert(66)
    inset.insert(100)
    inset.insert(12)

    print(f"First Round - unique numbers: {inset}")

    print(f"After checking - {inset.member(10)}")
    print(f"After checking - {inset.member(30)}")
    print(f"After checking - {inset.member(8)}")

    inset.remove(30)
    inset.remove(35)
    print(f"Second Round - after removing elements: {inset}")

    inset.remove(64)

    print(f"Last Round - left elements: {inset}")


if __name__ == "__main__":
    main()
