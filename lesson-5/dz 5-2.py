with open("textfile.txt", "r") as my_file:
    num = 0
    for line in my_file.readlines():
        print(f'{line.strip()} - длина стороки: {len(line)} символа')
        num += 1
    print(f'Количество сток в файле: {num}')
