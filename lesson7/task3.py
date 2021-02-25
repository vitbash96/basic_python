class Cell:
    def __init__(self, quantity: int):
        self.quantity = quantity

    def __add__(self, other: 'Cell') -> 'Cell':
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other: 'Cell') -> 'Cell':
        if self.quantity > other.quantity:
            return Cell(self.quantity - other.quantity)
        else:
            print('not possible')

    def __mul__(self, other: 'Cell') -> 'Cell':
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other: 'Cell') -> 'Cell':
        return Cell(self.quantity // other.quantity)

    def make_order(self, myrow: int) -> str:
        body = self.quantity // myrow
        tail = self.quantity % myrow
        return '\n'.join(['*' * myrow] * body + (['*' * tail] if tail > 0 else []))

    def __str__(self) -> str:
        return f'There are {self.quantity} cells  in the cell '


a = Cell(22)
b = Cell(11)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.make_order(6))
