import math


class Cell:
    def __init__(self, cell_count):
        self.cell_count = int(cell_count)

    def __add__(self, other):
        self.cell_count += int(other)

    def __sub__(self, other):
        if self.cell_count >= int(other):
            self.cell_count -= int(other)
        else:
            print('Ошибка. Разность количества ячеек должна быть больше нуля')

    def __mul__(self, other):
        self.cell_count *= int(other)

    def __truediv__(self, other):
        self.cell_count /= int(other)
        self.cell_count = int(round(self.cell_count, 0))

    def make_order(self):
        order = self.cell_count
        num_rows = math.ceil(order / 5)
        for line in range(num_rows):
            if order // 5 >= 1:
                result = f'*****'
                print(result)
            else:
                result = ''
                for i in range(order % 5):
                    result += '*'
                print(result)
            order -= 5


cell_calc = Cell(23)

cell_calc.make_order()

print('\n')
cell_calc + 5
print(cell_calc.cell_count)
cell_calc - 8
print(cell_calc.cell_count)
cell_calc * 2
print(cell_calc.cell_count)
cell_calc / 5
print(cell_calc.cell_count, '\n')

cell_calc.make_order()
