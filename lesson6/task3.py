class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return ' '.join([self.name, self.surname])

    def get_total_income(self):
        return sum(self._income.values())


test_data = [{'name': 'Max',
              'surname': 'Power',
              'position': 'CEO',
              'wage': 200000,
              'bonus': 300000},
             {'name': 'Eveline',
              'surname': 'Johnson',
              'position': 'CFO',
              'wage': 150000,
              'bonus': 50000}]

for i in test_data:
    a = Position(**i)
    print(a.name)
    print(a.surname)
    print(a.position)
    print(f'Full name: {a.get_full_name()}')
    print(f'Total income: {a.get_total_income()}')
