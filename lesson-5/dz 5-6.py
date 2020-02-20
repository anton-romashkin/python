import re

group_dict = {}

with open("study.txt", "r") as workbook:
    for line in workbook.readlines():
        work_list = (line.strip().split(':'))
        numbers = re.findall(r'\d+', work_list[1])
        group_dict[work_list[0]] = sum(map(int, numbers))
    print(group_dict)

"""
study.txt content:

Информатика: 100(л) 50(пр) 20(лаб)
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
"""
