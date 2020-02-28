class Worker:
    def __init__(self):
        self.name = 'Bill'
        self.surname = 'Brown'
        self.position = 'supply manager'
        self._income = worker_income['wage'] + worker_income['bonus']


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_income(self):
        print(f'{self._income}')


worker_income = {'wage': 10000, 'bonus': 5000}

personal_info = Position()
personal_info.get_full_name()
personal_info.get_income()
