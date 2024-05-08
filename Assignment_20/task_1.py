# This program reads JSON file. The program discovers an error. If there does not
# exist a file prints the informative text: "The JSON file does not exist".
# If the JSON file exists the program calculates the average salary for each department
# for the departments in the file. The program discovers potential errors.
# The program prints the calculated average salaries on the screen and writes in a JSON file
# avg_salary.json in the following format:
#                {
#                   "<department_name>": "<average_salary>",
#                   "<department_name>": "<average_salary>"
#                }

import json
import random


def generate_random_json(json_random_file, departments, employees):
    data = {}
    for department in departments:
        num_employees = random.randint(2, 6)
        data[department] = []
        for _ in range(num_employees):
            data[department].append(
                {
                    'name': random.choice(employees),
                    'salary': random.randint(1000, 8000)
                })

    with open(json_random_file, 'w') as file:
        json.dump(data, file, indent=4)


def calculate_avg_salary(data):
    avg_salaries = {}
    for department, employees in data.items():
        salaries = [employee['salary'] for employee in employees]
        avg_salaries[department] = sum(salaries) / len(salaries)
    return avg_salaries


def main():
    json_random_file = 'employees.json'
    avg_salary_file = 'avg_salary.json'
    departments = ['HR', 'IT', 'Finance', 'Marketing', 'Operations']
    employees = ["Sky", "Emma", "Elena", "Alice", "Barbara", "Sebastian",
                 "Rafael", "Tomas", "Eve", "Victoria", "Darla", "Blue",
                 "Alexander", "Katara"]

    generate_random_json(json_random_file, departments, employees)
    with open(json_random_file) as file:
        data = json.load(file)

    try:
        with open(json_random_file) as file:
            data = json.load(file)
    except FileNotFoundError:
        print("The JSON file does not exist")
        return

    avg_salaries = calculate_avg_salary(data)

    for department, avg_salary in avg_salaries.items():
        print(f"Average salary for {department}: {avg_salary}")

    with open(avg_salary_file, 'w') as file:
        json.dump(avg_salaries, file, indent=4)


if __name__ == "__main__":
    main()
