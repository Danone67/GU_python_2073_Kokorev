from random import choice


class Car:
    side = ["направо", "налево"]

    def __init__(self, name, color, speed, police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = police

    def go(self):
        print(f'{self.name}: Поехала')

    def stop(self):
        print(f'{self.name}: Экстренно остановилась')

    def turn(self):
        print(f'{self.name}: поворачивает {choice(self.side)}')

    def show_speed(self):
        return f'{self.name}: летит с бешенной скоростью: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        return f'{self.name}: Скорость: {self.speed}. Надо бы притормозить!' \
            if self.speed > 60 else super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        return f'{self.name}: Скорость: {self.speed}. Она сейчас развалиться!' \
            if self.speed > 40 else super().show_speed()


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, name, color, speed, police=True):
        super().__init__(name, color, speed, police)


police_car = PoliceCar('Лада Веста', 'Серая', 100)
work_car = WorkCar('Ford Focus', 'Белый', 40)
sport_car = SportCar('AUDI RS6', 'Красный', 120)
town_car = TownCar('Kia Picanto', 'Чёрный', 65)

cars = [police_car, work_car, sport_car, town_car]
for i in cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()
