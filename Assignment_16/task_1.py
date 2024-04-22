# The following groups of numbers are temperatures of morning,
# afternoon and evening of each day of the week.

# I. Monday - (33, 34, 28)
# II. Tuesday - (24, 31, 27)
# III. Wednesday - (24, 23, 27)
# IV. Thursday - (28, 32, 34)
# V. Friday - (33, 21, 28)
# VI. Saturday - (20, 25, 31)
# VII. Sunday - (21, 31, 28)

# This program finds the arithmetic mean of temperatures, also maximum and
# minimum temperatures of each day.
# Also, the program calculates the arithmetic mean of
# temperatures of the week (based on the arithmetic mean of each day).


def get_daily_and_week_temperature_stats(days_of_week, temperatures):
    daily_means_sum = 0
    for c in range(len(temperatures)):
        print(f"Day: {days_of_week[c]}")
        print(f"Temperatures: {temperatures[c]}")
        print(f"The arithmetic mean of the temperatures: {sum(temperatures[c]) / len(temperatures[c])}")
        print(f"The minimum temperature: {min(temperatures[c])}")
        print(f"The maximum temperature: {max(temperatures[c])}")
        daily_means_sum += sum(temperatures[c]) / len(temperatures[c])

    week_mean = daily_means_sum / len(temperatures)
    print(f"\nThe arithmetic mean of temperatures of the week: {week_mean}")


def main():
    temperatures = ((33, 34, 28), (24, 31, 27), (24, 23, 27), (28, 32, 34), (33, 21, 28), (20, 25, 31), (21, 31, 28))
    days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    get_daily_and_week_temperature_stats(days_of_week, temperatures)


if __name__ == "__main__":
    main()
