from abc import ABC, abstractmethod


class Coat:
    def __init__(self, size):
        self.consumption = float(size) / 6.5 + 0.5


class Suit:
    def __init__(self, size):
        self.consumption = 2 * float(size) + 0.3


class Clothes_abstract(ABC):
    def __init__(self):
        self.cons_list = []
        self.cons_sum = 0

    @abstractmethod
    def add_coat(self, size):
        self.cons_list.append(Coat(size).consumption)

    @abstractmethod
    def add_suit(self, size):
        self.cons_list.append(Suit(size).consumption)

    @property
    def get_consumption(self):
        for i in self.cons_list:
            self.cons_sum += i
        return f'Для производства одежды понадобится: ' \
               f'{round(self.cons_sum, 2)} ткани'


class Clothes(Clothes_abstract):
    def __init__(self):
        super().__init__()

    def add_coat(self, size):
        self.cons_list.append(Coat(size).consumption)

    def add_suit(self, size):
        self.cons_list.append(Suit(size).consumption)

    @property
    def get_consumption(self):
        for i in self.cons_list:
            self.cons_sum += i
        return f'Для производства одежды понадобится: ' \
               f'{round(self.cons_sum, 2)} метров ткани'


cloth = Clothes()
print(cloth.get_consumption)
cloth.add_coat(8)
print(cloth.get_consumption)
cloth.add_suit(5)
cloth.add_suit(3)
print(cloth.get_consumption)
