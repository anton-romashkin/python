sum_list = 0
while True:
    user_list = input('Введите числа через пробел. Для выхода введите q. ')
    if 'q' in user_list.lower():
        user_list = list(user_list.split())
        user_list[user_list.index('q')] = 0
        sum_list = sum_list + sum(map(int, user_list))
        print(f'Сумма: {sum_list}\nЗавершение программы.')
        break
    else:
        sum_list = sum_list + sum(map(int, list(user_list.split())))
        print(f'Сумма: {sum_list}')
