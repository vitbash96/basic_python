from abc import ABC, abstractmethod


class Clothes(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def count_fabric(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    @property
    def name(self):
        print('Coat')

    @property
    def count_fabric(self):
        return self.V / 6.5 + 5

    def __str__(self):
        return f'{self.count_fabric} m of fabric require for size {self.V}'


class Suit(Clothes):
    def __init__(self, H):
        self.H = H

    @property
    def name(self):
        print('Suit')

    @property
    def count_fabric(self):
        return self.H * 2 + 0.3

    def __str__(self):
        return f'{self.count_fabric} m of fabric require for size {self.H}'


coat = Coat(180)
coat.name
coat.count_fabric
print(coat)

suit = Suit(183)
suit.name
suit.count_fabric
print(suit)
