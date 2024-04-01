# This program gets the year, month and day from the user (it is the date when
# the user bought a bitcoin).
# The program gets also an amount of money the user paid for the bitcoin on that date (in dollars).
# The program prints the amount of money in dollars which the user made a profit or lost
# taking into consideration the price of bitcoin now.
# The program using module forex-python for Foreign exchange rates and currency conversion.

from forex_python.bitcoin import BtcConverter
from datetime import datetime

year = int(input("Enter the year you bought a Bitcoin: "))
month = int(input("Enter the month you bought a Bitcoin: "))
day = int(input("Enter the day you bought a Bitcoin: "))
purchase_price = float(input("Enter the amount of money you paid for the bitcoin (in dollars): "))


def get_profit_loss(year, month, day, purchase_price):
    b = BtcConverter()
    purchase_date = datetime(year, month, day)

    previous_price = b.get_previous_price('USD', purchase_date)
    current_price = b.get_latest_price('USD')

    purchased_bitcoin = purchase_price / previous_price
    current_value = purchased_bitcoin * current_price
    profit_loss = current_value - purchase_price

    return profit_loss, current_value


profit_loss, current_value = get_profit_loss(year, month, day, purchase_price)

if profit_loss > 0:
    print(f"You made a profit of ${profit_loss:.2f}, and your Bitcoin is now worth ${current_value:.2f}.")
else:
    print(f"You lost ${-profit_loss:.2f}, and your Bitcoin is now worth ${current_value:.2f}.")
