current_result = int(input('Сколько километров спортсмен пробегает сейчас? '))
desired_result = int(input('Сколько километров спортсмен хочет пробегать? '))
day = 1
while current_result < desired_result:
    current_result *= 1.1
    day += 1

print(f'Спотртсмен достигнет результата на {day} день')
