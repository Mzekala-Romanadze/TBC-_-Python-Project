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


def calculate_daily_means(days_of_week, temperatures):
    for c in range(len(temperatures)):
        for _ in range(1):
            print(f"Day: {days_of_week[c]}")
            print(f"Temperatures: {temperatures[c]}")
            print(f"The arithmetic mean of the temperatures: {sum(temperatures[c]) / len(temperatures[c])}")
            print(f"The minimum temperature: {min(temperatures[c])}")
            print(f"The maximum temperature: {max(temperatures[c])}")


def calculate_week_mean(temperatures):
    sum_mean_temps = 0
    for c in range(len(temperatures)):
        for i in range(1):
            sum_mean_temps += sum(temperatures[c]) / len(temperatures[c])
    week_mean = sum_mean_temps / len(temperatures)
    return week_mean


def main():
    temperatures = ((33, 34, 28), (24, 31, 27), (24, 23, 27), (28, 32, 34), (33, 21, 28), (20, 25, 31), (21, 31, 28))
    days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    week_mean = calculate_week_mean(temperatures)
    calculate_daily_means(days_of_week, temperatures)

    print(f"\nThe arithmetic mean of temperatures of the week: {week_mean}")


if __name__ == "__main__":
    main()
