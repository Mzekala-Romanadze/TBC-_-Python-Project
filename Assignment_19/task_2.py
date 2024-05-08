# This program reads purchase details in data.txt (same file from task_1).
# The program finds:
#           1. the customer (if more than one, list of customers) who purchased
#           maximum number of product in one purchase.
#           2. the customer (if more than one, list of customers) who paid
#           maximum price in all purchases.
#           3. the arithmetic mean of the purchase prices.
#           4. the arithmetic mean of the purchase quantities.
#           5. the product (if more than one, list of products) maximum number of which were sold.
# The program saves the above information in dictionary data structure and
# then writes the information in stats.json file.
# The stats.json file is formatted to be easily readable.

import json


def find_statistical_information():
    max_products_customer = []
    max_price_customer = []
    total_prices = 0
    total_quantities = 0
    product_counts = {}

    with open("data.txt", "r") as file:
        lines = file.readlines()

    if lines:
        for line in lines:
            user_name, product_name, amount, price = line.strip().split(',')
            amount = int(amount)
            price = float(price)

            # Update max_products_customer
            if not max_products_customer or amount > max_products_customer[0][1]:
                max_products_customer = [((user_name, product_name), amount)]
            elif amount == max_products_customer[0][1]:
                max_products_customer.append(((user_name, product_name), amount))

            # Update max_price_customer
            if not max_price_customer or price > max_price_customer[0][1]:
                max_price_customer = [((user_name, product_name), price)]
            elif price == max_price_customer[0][1]:
                max_price_customer.append(((user_name, product_name), price))

            # Update total prices and quantities
            total_prices += price
            total_quantities += amount

            # Update product_counts
            if product_name in product_counts:
                product_counts[product_name] += amount
            else:
                product_counts[product_name] = amount

        # Calculate the arithmetic mean of the purchase prices
        mean_price = total_prices / len(lines)

        # Calculate the arithmetic mean of the purchase quantities
        mean_quantity = total_quantities / len(lines)

    else:
        mean_price = 0
        mean_quantity = 0

    # Write statistics in dictionary data structure
    stats = {
        "max_products_customer": max_products_customer,
        "max_price_customer": max_price_customer,
        "mean_price": mean_price,
        "mean_quantity": mean_quantity,
        "max_sold_product": [key for key, value in product_counts.items() if value == max(product_counts.values())]
    }

    # Write statistics to stats.json
    with open("stats.json", "w") as json_file:
        json.dump(stats, json_file, indent=4)

    print("Statistics saved in stats.json")


def main():
    find_statistical_information()


if __name__ == "__main__":
    main()
