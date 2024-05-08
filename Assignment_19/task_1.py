# Firstly, the program creates data.txt file with randomly generated information about the purchases.
# Then the program reads data.txt file (contains the details of purchased
# products). In the file the details are separated with comma ',' and
# are written in the following order: user_name, product_name, amount, price (of one item).
# The program creates 2 new file: small.txt and high.txt.
#           => In small.txt file: there is written the purchases of which price is less than 10.
#           => In high.txt file: there is written the rest purchases.


import random


def create_data_file(user_names, product_names):
    with open("data.txt", "w") as file:
        for user in range(len(user_names)):
            user_name = user_names[user]
            product_name = random.choice(product_names)
            amount = random.randint(1, 10)  # number of kilos
            price = round(random.uniform(1, 10), 2)  # price of one kilo
            file.write(f"{user_name},{product_name},{amount},{price}\n")


def create_small_and_high_files():
    with open("data.txt", "r") as file:
        lines = file.readlines()

    with open("small.txt", "w") as small_file, open("high.txt", "w") as high_file:
        for line in lines:
            user_name, product_name, amount, price = line.strip().split(',')
            amount = int(amount)
            price = float(price)
            total_price = amount * price

            if total_price < 10:
                small_file.write(f"{user_name}, {product_name}, {amount}, {price}\n")
            else:
                high_file.write(f"{user_name}, {product_name}, {amount}, {price}\n")


def main():
    user_names = ["Sky", "Emma", "Elena", "Alice", "Barbara", "Sebastian", "Rafael", "Tomas", "Eve",
                  "Victoria", "Darla", "Blue", "Alexander", "Katara"]
    product_names = ["Apple", "Banana", "Orange", "Broccoli", "Watermelon", "Strawberry", "Cherry",
                     "Plum", "Mango", "Avocado", "Pineapple", "Lime", "Sweet potatoes", "Mushrooms"]

    create_data_file(user_names, product_names)
    create_small_and_high_files()


if __name__ == "__main__":
    main()
