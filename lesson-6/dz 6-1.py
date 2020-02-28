import time


class TrafficLight:
    _color = 'red'

    def running(self):
        while True:
            print(self._color)
            if self._color == 'green':
                time.sleep(5)
                self._color = 'red'
            elif self._color == 'yellow':
                time.sleep(2)
                self._color = 'green'
            elif self._color == 'red':
                time.sleep(7)
                self._color = 'yellow'


start_light = TrafficLight()
start_light.running()
