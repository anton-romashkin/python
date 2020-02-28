class Stationery:
    def __init__(self):
        title = 'default'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        super().__init__()
        title = 'pen'

    def draw(self):
        print('Отрисовка ручкой')


class Pencil(Stationery):
    def __init__(self):
        super().__init__()
        title = 'pen'

    def draw(self):
        print('Отрисовка карандашом')


class Handle(Stationery):
    def __init__(self):
        super().__init__()
        title = 'pen'

    def draw(self):
        print('Отрисовка маркером')


default = Stationery()
default.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
