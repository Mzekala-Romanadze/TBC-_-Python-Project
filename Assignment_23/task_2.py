# This program has a class Queue being a data structure similar to the Stack.
# It has insert and remove methods for adding and removing elements in the list.
# The first element added should be returned first - FIFO (First In First Out).

class Queue:
    def __init__(self):
        self.elements = []

    def insert(self, element):
        self.elements.append(element)

    def remove(self):
        if not self.elements:
            raise IndexError("Queue is empty.")
        return self.elements.pop(0)


def main():
    q = Queue()
    q.insert(30)
    q.insert(60)
    q.insert(80)
    print(q.remove())
    print(q.remove())
    print(q.remove())
    print(q.remove())


if __name__ == '__main__':
    main()
