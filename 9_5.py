class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Ручка рисует {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Карандаш рисует {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Маркер рисует {self.title}'


pen = Pen('Круг')
print(pen.draw())
pencil = Pencil('Квадрат')
print(pencil.draw())
handle = Handle('Овал')
print(handle.draw())
