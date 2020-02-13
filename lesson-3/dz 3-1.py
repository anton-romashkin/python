def func_divide(num, divident):
    try:
        return num / divident
    except ZeroDivisionError:
        print('Ошибка. Деление на ноль')
        return None


a = float(input('Введите делимое число: '))
b = float(input('Введите делитель: '))
print(func_divide(a, b))
