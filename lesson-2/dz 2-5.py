rating = [7, 5, 3, 3, 2]
print(rating)
new_element = int(input('Введите число: '))
rating.append(new_element)
print(sorted(rating, reverse=True))
