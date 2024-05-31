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


def read_json_file(input_file):
    try:
        with open(input_file, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("The input JSON file does not exist.")
        exit()
    except json.decoder.JSONDecodeError:
        print("The file is empty.")
        exit()



def calculate_average_salary(department):
    salaries = []
    for employee in department.get('employees', []):
        try:
            salary = float(employee['salary'])
            salaries.append(salary)
        except ValueError:
            salary = employee['salary']
            if salary == "None":
                salaries.append(0)
    if salaries:
        return sum(salaries) / len(salaries)
    else:
        return 0


def create_new_file(data, output_file):
    average_salaries = {}

    for _, department in data.items():
        average_salary = calculate_average_salary(department)
        average_salaries[department["name"]] = average_salary

    with open(output_file, 'w') as file:
        json.dump(average_salaries, file, indent=4)


def main():
    input_file = 'employees.json'
    output_file = 'avg_salary.json'

    input_file_data = read_json_file(input_file)
    create_new_file(input_file_data, output_file)


if __name__ == "__main__":
    main()
