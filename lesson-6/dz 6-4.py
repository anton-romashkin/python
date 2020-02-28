class Car:
    def __init__(self):
        self.speed = 60
        self.color = 'red'
        self.name = 'Nissan'
        self.is_police = False

    def go(self):
        print('Машина поехала')

    def stop(self):
        self.speed = 0
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self):
        super().__init__()
        self.speed = 75
        self.color = 'orange'
        self.name = 'Lexus'

    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print('Внимание! Превышение скорости.')


class SportCar(Car):
    def __init__(self):
        super().__init__()
        self.speed = 120
        self.color = 'blue'
        self.name = 'Ferrari'


class WorkCar(Car):
    def __init__(self):
        super().__init__()
        self.speed = 35
        self.color = 'black'
        self.name = 'Dodge'

    def show_speed(self):
        print(self.speed)
        if self.speed > 40:
            print('Внимание! Превышение скорости.')

class PoliceCar(Car):
    def __init__(self):
        super().__init__()
        self.speed = 80
        self.color = 'white'
        self.name = 'Ford'
        self.is_police = True


test = TownCar().show_speed()
