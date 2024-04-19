# The program removes all strings with more than 3 characters in the list
# and after removing strings prints new list (elements in uppercase).


def remove_extra(my_list):
    new_list = list(filter(lambda c: len(c) <= 3, my_list))
    return [c.upper() for c in new_list]


def main():
    my_list = ["sun", "moon", "star", "earth", "universe", "cat", "rabbit", "dog", "car", "cup", "bed", "box", "key"]
    new_list = remove_extra(my_list)

    print("Original version of my list: ", my_list)
    print("New version of my list: ", new_list)


if __name__ == "__main__":
    main()
