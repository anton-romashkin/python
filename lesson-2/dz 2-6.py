goods_structure = []
goods_num = int(input('Введите количество товаров: '))
i = 1
while i <= goods_num:
    goods_name = input('Введите наименование товара: ')
    goods_value = int(input('Введите цену товара: '))
    goods_quantity = int(input('Введите количество товара: '))
    goods_unit = input('Введите единицу измерения: ')
    goods_set = {'название': goods_name, 'цена': goods_value, 'количество': goods_quantity, 'ед': goods_unit}
    goods_tuple = (i, goods_set)
    goods_structure.append(goods_tuple)
    i += 1

goods_analytics = {}
goods_names = []
goods_prices = []
goods_quantities = []
goods_units = []

for product in goods_structure:
    for key, val in product[1].items():
        if key == 'название':
            goods_names.append(val)
            goods_analytics[key] = list(set(goods_names))
        elif key == 'цена':
            goods_prices.append(val)
            goods_analytics[key] = list(set(goods_prices))
        elif key == 'количество':
            goods_quantities.append(val)
            goods_analytics[key] = list(set(goods_quantities))
        elif key == 'ед':
            goods_units.append(val)
            goods_analytics[key] = list(set(goods_units))

print(goods_analytics)
