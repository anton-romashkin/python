user_text = list(input('Введите несколько слов: ').split())
for ind, word in enumerate(user_text):
    print(ind, word[:10])
