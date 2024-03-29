# This program gets the year, month and day of birth from the user
# and prints the day on which the person is born.

import datetime


def get_birthdate():
    while True:
        try:
            year = int(input("Enter your birth year: "))
            month = int(input("Enter your birth month: "))
            day = int(input("Enter your birth day: "))

            # Valid date
            if not 1 <= month <= 12 or not 1 <= day <= 31:
                raise ValueError("Invalid date. Please enter a valid month (1-12) and day (1-31).")

            birthdate = datetime.date(year, month, day)
            return birthdate

        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again with valid information.")


def get_day_of_week(birthdate):
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return day_names[birthdate.weekday()]


def result():
    birthdate = get_birthdate()
    day_of_week = get_day_of_week(birthdate)
    print(f"You were born on a {day_of_week}.")


if __name__ == "__main__":
    result()
