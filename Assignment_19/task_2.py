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


def read_data_file(filename):
    with open(filename, "r") as file:
        data = file.readlines()
    return data


def find_max_product_customer(data):
    max_product_customer = []
    max_product_amount = 0
    customer_purchase_amount = {}

    for line in data:
        customer, _, amount, _ = line.strip().split(',')
        amount = int(amount)

        if customer in customer_purchase_amount:
            customer_purchase_amount[customer] += amount
        else:
            customer_purchase_amount[customer] = amount

        if amount > max_product_amount:
            max_product_amount = amount

    for customer, amount in customer_purchase_amount.items():
        if amount == max_product_amount:
            max_product_customer.append(customer)

    return max_product_customer, max_product_amount


def find_max_payment_customer(data):
    max_payment_customer = []
    customer_total_payment = {}

    for line in data:
        user_name, _, amount, price = line.strip().split(',')
        amount = int(amount)
        price = float(price)

        if user_name in customer_total_payment:
            customer_total_payment[user_name] += price * amount
        else:
            customer_total_payment[user_name] = price * amount

    max_payment = max(customer_total_payment.values())
    for customer, total_payment in customer_total_payment.items():
        if total_payment == max_payment:
            max_payment_customer.append(customer)

    return max_payment_customer, max_payment


def calculate_mean_of_purchase_price(data):
    total_purchase_price = 0
    counter = 0
    for line in data:
        _, _, amount, price = line.strip().split(',')
        amount = int(amount)
        price = float(price)
        total_payment = amount * price
        total_purchase_price += total_payment
        counter += amount

    mean_price = total_purchase_price / counter
    return mean_price


def calculate_mean_of_purchase_amount(data):
    total_purchases = 0
    counter = 0
    for line in data:
        _, _, amount, _ = line.strip().split(',')
        total_purchases += int(amount)
        counter += 1

    mean_amount = total_purchases / counter
    return mean_amount


def find_bestseller_product(data):
    product_amount_data = {}
    bestseller_product = []

    for line in data:
        _, product_name, amount, _ = line.strip().split(',')
        amount = int(amount)

        if product_name in product_amount_data:
            product_amount_data[product_name] += amount
        else:
            product_amount_data[product_name] = amount

    max_product_amount = max(product_amount_data.values())
    for product, amount in product_amount_data.items():
        if amount == max_product_amount:
            bestseller_product.append(product)

    return bestseller_product, max_product_amount


def merge_statistical_info(data) -> dict:
    max_product_customer, max_amount = find_max_product_customer(data)
    max_payment_customer, max_payment = find_max_payment_customer(data)
    mean_price = calculate_mean_of_purchase_price(data)
    mean_amount = calculate_mean_of_purchase_amount(data)
    bestseller_product, amount = find_bestseller_product(data)

    merged_data = {
        "Customer(s) who purchased maximum amount of products": max_product_customer,
        "Maximum amount purchased by 1 customer": max_amount,
        "Customer(s) who made maximum payment": max_payment_customer,
        "Maximum purchase payment": max_payment,
        "Mean of purchase prices": mean_price,
        "Mean of purchase amount": mean_amount,
        "Bestseller product": bestseller_product,
        "Amount of sold bestseller product": amount
    }
    return merged_data


def load_data_into_json_file(data, output_file):
    merged_data = merge_statistical_info(data)

    with open(output_file, "w") as json_file:
        json.dump(merged_data, json_file, indent=4)


def main():
    input_file = "data.txt"
    output_file = "stats.json"

    data = read_data_file(input_file)
    load_data_into_json_file(data, output_file)


if __name__ == "__main__":
    main()
