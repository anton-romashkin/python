new_string = 'str'
with open("new_file.txt", "w") as workbook:
    while len(new_string) > 0:
        new_string = (input('Введите текст для записи в файл: '))
        workbook.write(f'{new_string}\n')
