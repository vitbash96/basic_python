class Road:
    __unit_mass = 0.025

    def __init__(self, length, width):
        self._length_ = float(length)
        self._width_ = float(width)

    def get_mass(self, thickness):
        return self._length_ * self._width_ * thickness * self.__unit_mass


a = Road(5000, 20)
print(a.get_mass(5))
