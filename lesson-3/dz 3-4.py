def neg_power(x, y):
    #  реализация через оператор **
    result = x ** y
    print(f'{result} - через оператор **')

    #  реализация через цикл
    i = -1
    current_power = 1
    while i >= y:
        current_power = current_power * x
        i -= 1
    result = 1 / current_power
    print(f'{result} - через цикл')


neg_power(2, -4)
