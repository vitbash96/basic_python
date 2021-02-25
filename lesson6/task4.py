class Car:
    def __init__(self, name, color, speed=0, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = ''

    def go(self, speed):
        self.speed = speed
        return print(f'the car has started')

    def stop(self):
        self.speed = 0
        return f'the car has stopped'

    def turn(self, direction):
        if direction == 'right':
            print('right turn')

        elif direction == 'left':
            print('left turn')

        else:
            print('not an arrow button!')

    def show_speed(self):
        print(f'The current speed is: {self.speed}')


class TownCar(Car):
    _speed_limit_TC = 60

    def show_speed(self):
        print(f'The current speed is: {self.speed}')
        if self.speed > self._speed_limit_TC:
            print(f'You exceed the speed limit')


class WorkCar(Car):
    _speed_limit_WC = 40

    def show_speed(self):
        print(f'The current speed is: {self.speed}')
        if self.speed > self._speed_limit_WC:
            print(f'You exceed the speed limit')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, *args, is_police):
        super().__init__(*args)
        if not is_police:
            print("Don't pretend to be the police")
        else:
            print('#########################')
            print('You are in the Police Car')

a = TownCar('kia', 'red')
print(a.name)
print(a.color)
a.go(50)
a.show_speed()
a.turn('left')
a.go(80)
a.show_speed()

b = PoliceCar('vw', 'white', is_police=True)
b.go(60)
b.show_speed()

# kia = TownCar('kia', 'red', 60, True)
# kia.go(80)
# kia.show_speed()
# bmw = SportCar('bmw', 'black', 90, False)
# vw = WorkCar('VW', 'grey')
