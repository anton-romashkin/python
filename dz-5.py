revenue = int(input('Выручка: '))
costs = int(input('Издержки: '))

while revenue > costs:
    print('Фирма приносит доход')
    profitability = int((revenue - costs) / revenue * 100)
    print(f'Рентабельность: {profitability}%\n')
    employees = int(input('Сколько сотрулников работает в фирме: '))
    profit_for_person = (revenue - costs) / employees
    print(f'Прибыль на одного сотрудника: {profit_for_person}')
    break
else:
    print('Фирма убыточна')
