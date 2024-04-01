# This program gets date as a string (year, month, day, hour,
# minute, second, microsecond, timezone) in format: YYYY-MM-DDT00:00:00.000000-00:00
# from the user and # turns it into different format.

from datetime import datetime

date = input("Enter date: (YYYY-MM-DDT00:00:00.000000-00:00) ")

input_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f%z")
output_date = input_date.strftime("%d-%m-%Y %I:%M:%S %z").replace(" 0", " ")

timezone = input_date.strftime("%z")
output_date = output_date.replace(timezone, timezone[:3].replace("0", "", 1))

print("Output:", output_date)
