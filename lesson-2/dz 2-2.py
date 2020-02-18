my_list = list(range(int(input('Введите количество элементов списка: '))))
stage = 1
i = 0
print(my_list)

while stage <= len(my_list) // 2:
    my_list[i + 1], my_list[i] = my_list[i], my_list[i + 1]
    stage += 1
    i += 2
print(my_list)
