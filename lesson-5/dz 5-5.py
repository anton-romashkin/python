from random import randint

random_string = ' '.join([str(randint(1, 100)) for i in range(0, 15)])

with open("new_file.txt", "w") as workbook:
    workbook.write(random_string)
with open("new_file.txt", "r") as workbook:
    num_string = workbook.readline()
    print(f'Сумма: {sum(map(int, list(num_string.split())))}')
