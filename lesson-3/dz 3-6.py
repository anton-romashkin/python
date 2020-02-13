def my_title(text):
    return text.title()


name = my_title('jack')
user_string = f'all work and no play makes {name} a dull boy'

#  применяет функцию my_title отдельно к каждому слову текста
format_string = ' '.join(list(map(my_title, list(user_string.split()))))
print(format_string)

# тот же результат
# print(user_string.title())
# print(my_title(user_string))
