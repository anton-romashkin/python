number = int(input('Введите число: '))
num_max = 0

while number > 0:
    if num_max <= number % 10:
        num_max = number % 10
    number = number // 10

print(num_max)
