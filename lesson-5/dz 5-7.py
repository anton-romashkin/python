import json
from statistics import mean

companies_dict = {}
average_profit = {}
profit_list = []
main_list = []

with open("firms.txt", "r") as workbook:
    for line in workbook.readlines():
        work_list = (line.strip().split())
        name = work_list[0]
        profit = int(work_list[2]) - int(work_list[3])
        companies_dict[name] = profit
        print(f'{name} - прибыль: {profit}')
        if profit > 0:
            profit_list.append(profit)
    print(f'Средняя прибыль: {mean(profit_list)}')
    average_profit['average_profit'] = mean(profit_list)
    main_list.append(companies_dict)
    main_list.append(average_profit)
    print(main_list)

with open("my_json.json", "w") as write_f:
    json.dump(main_list, write_f)
