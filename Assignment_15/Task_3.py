# The program removes all strings with more than 3 characters in the list
# and after removing strings prints new list (elements in uppercase).


def remove_extra(my_list):
    new_list = []
    for c in my_list:
        if len(c) <= 3:
            new_list.append(c.upper())
    return new_list


def main():
    my_list = ["sun", "moon", "star", "earth", "universe", "cat", "rabbit", "dog", "car", "cup", "bed", "box", "key"]
    new_list = remove_extra(my_list)

    print("Original version of my list: ", my_list)
    print("New version of my list: ", new_list)


if __name__ == "__main__":
    main()
