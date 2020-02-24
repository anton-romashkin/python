class Road:
    def __init__(self, cm_mass, thickness):
        self._length = 20
        self._width = 5000
        self.mass = cm_mass
        self.thick = thickness

    def calc_mass(self):
        road_mass = (self._length * self._width * self.mass * self.thick) / 1000
        print(road_mass)


my_road = Road(25, 5)
my_road.calc_mass()
