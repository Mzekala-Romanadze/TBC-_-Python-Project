# This program has function 'midpoint(x1, y1, x2, y2)'
# which calculates middle point between x and y and returns it in tuple structure.
# The formula to calculate middle point is: (x1 + x2) / 2 , (y1 + y2) / 2)
# The main function includes examples to demonstrate the working of the midpoint function.


def midpoint(x_1, y_1, x_2, y_2):
    mid_x = (x_1 + x_2) / 2
    mid_y = (y_1 + y_2) / 2
    return mid_x, mid_y


def main():
    x_1 = int(input("Enter x_1: "))
    y_1 = int(input("Enter y_1: "))
    x_2 = int(input("Enter x_2: "))
    y_2 = int(input("Enter y_2: "))

    midpoint_of_x_and_y = midpoint(x_1, y_1, x_2, y_2)
    print(f"Midpoint between ({x_1}, {y_1}) and ({x_2}, {y_2}) is {midpoint_of_x_and_y}")

    # Example 1 to demonstrate working of midpoint function
    example_1_x_1, example_1_y_1 = 6, 8
    example_1_x_2, example_1_y_2 = 12, 16
    midpoint_example_1 = midpoint(example_1_x_1, example_1_y_1, example_1_x_2, example_1_y_2)
    print(f"Example 1: Midpoint between ({example_1_x_1}, {example_1_y_1}) and ({example_1_x_2}, {example_1_y_2}) is {midpoint_example_1}")

    # Example 2 to demonstrate working of midpoint function
    example_2_x_1, example_2_y_1 = 0, 0
    example_2_x_2, example_2_y_2 = 12, 24
    midpoint_example_2 = midpoint(example_2_x_1, example_2_y_1, example_2_x_2, example_2_y_2)
    print(f"Example 2: Midpoint between ({example_2_x_1}, {example_2_y_1}) and ({example_2_x_2}, {example_2_y_2}) is {midpoint_example_2}")


if __name__ == "__main__":
    main()
