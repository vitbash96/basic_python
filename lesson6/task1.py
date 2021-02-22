from time import sleep


class TrafficLight:
    _colore = ['red', 'yellow', 'green']

    def running(self):
        for i in self._colore:
            if i == 'red':
                print(f'Red signal')
                sleep(7)
            elif i == 'yellow':
                print(f'Yellow signal')
                sleep(2)
            elif i == 'green':
                print(f'Green signal')
                sleep(10)


a = TrafficLight()
a.running()
