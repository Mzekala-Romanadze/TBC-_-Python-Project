# This program reads employee.json file (if the file does not exist
# the program prevents the error).
# To solve the problem the program is written by creating
# two classes: Department and Employee and their attributes are defined
# as they appear in the JSON file.
# For the Department class, there are following methods:
#               1. average - calculates and returns the average salary.
#               2. max - finds the maximum salary
#               3. min - finds the minimum salary
#               4. positions - counts how many employees work in each position and
#               returns a dict object with the format position - number of employees
# The object of the classes are created with data from the employee.json file.

import json


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = int(salary)


class Department:
    def __init__(self, name, description, employees):
        self.name = name
        self.description = description
        self.employees = employees

    def average(self):
        if not self.employees:
            return 0
        total_salary = sum(employee.salary for employee in self.employees)
        return total_salary / len(self.employees)

    def max(self):
        if not self.employees:
            return 0
        return max(employee.salary for employee in self.employees)

    def min(self):
        if not self.employees:
            return 0
        return min(employee.salary for employee in self.employees)

    def positions(self):
        position_count = {}
        for employee in self.employees:
            if employee.position in position_count:
                position_count[employee.position] += 1
            else:
                position_count[employee.position] = 1

        if not bool(position_count):
            position_count = {"No active positions": 0}

        return position_count


def read_json_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
        return None

    departments = []
    for dep_key, dep_data in data.items():
        employees = [Employee(employee['name'], employee['position'],
                              employee['salary']) for employee in dep_data['employees']]
        department = Department(dep_data['name'], dep_data['description'], employees)
        departments.append(department)

    return departments


def main():
    file_name = 'employee.json'
    departments = read_json_file(file_name)

    if departments:
        for department in departments:
            print(f"Department name: {department.name}")
            print(f"Description: {department.description}")
            print(f"=> Average salary: {department.average()}")
            print(f"=> Maximum salary: {department.max()}")
            print(f"=> Minimum salary: {department.min()}")
            print("Positions and number of employees: ", department.positions())


if __name__ == "__main__":
    main()
