def person_info(name, surname, birth_year, city, email, phone):
    print(f'{name} {surname}, год рождения: {birth_year}. '
          f'Проживает в городе {city}\nКонтакты: email - {email}, телефон - {phone}')


person_info(surname='Малкович', name='Джон', birth_year=1969, city='Берлин', email='john.malkovich@gmail@com', phone='+1 312 876 87 123')
