from statistics import mean

salaries_data = []
low_salary = []
with open("textfile.txt", "r") as employees:
    for employee in employees.readlines():
        person_info = employee.strip().split()
        if int(person_info[1]) < 20000:
            low_salary.append(person_info[0])
        salaries_data.append(int(person_info[1]))

print(f'Средняя величина дохода сотрудников - {mean(salaries_data)}')
print(f'Сотрудники, которые зарабатывают менее 20000: {low_salary[:]}')

"""
textfile.txt content:

Иванов 5000
Петров 6000
Сидоров 7000
Абрамович 100000
"""
