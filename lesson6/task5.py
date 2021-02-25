class Stationery:
    def __init__(self, title):
        self.title = title
        print(title)

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки. Ручка')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки. Карандаш')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки. Маркер')


pen = Pen('Зарисовка')
pen.draw()
pencil = Pencil('Зарисовка')
pencil.draw()
handle = Handle('Зарисовка')
handle.draw()