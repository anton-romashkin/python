num_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
result = []

with open("numbers.txt", "r") as my_num:
    for num_line in my_num.readlines():
        source_list = num_line.strip().split(' — ')
        result.append(f'{num_dict[source_list[0]]} — {source_list[1]}')
with open("numbers_translated.txt", "w") as workbook:
    for line in result:
        workbook.write(f'{line}\n')
