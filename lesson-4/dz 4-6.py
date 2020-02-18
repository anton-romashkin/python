from itertools import count
from itertools import cycle


def iterator_count():
    start_num = 5
    for i in count(start_num):
        if i > 15:
            break
        else:
            print(int(i))


def iterator_cycle():
    max_cycle = 1
    for el in cycle([1, 2, 3, 4, 5]):
        if max_cycle > 10:
            break
        else:
            print(el)
            max_cycle += 1
