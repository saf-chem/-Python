# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class TownCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} поехала!'.format(self.name))

    def stop(self):
        print('Машина {} остановилась!'.format(self.name))

    def turn(self, direction):
        print('Машина {} повернула {}!'.format(self.name, direction))


class SportCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} поехала!'.format(self.name))

    def stop(self):
        print('Машина {} остановилась!'.format(self.name))

    def turn(self, direction):
        print('Машина {} повернула {}!'.format(self.name, direction))


class WorkCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} поехала!'.format(self.name))

    def stop(self):
        print('Машина {} остановилась!'.format(self.name))

    def turn(self, direction):
        print('Машина {} повернула {}!'.format(self.name, direction))


class PoliceCar:
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} поехала!'.format(self.name))

    def stop(self):
        print('Машина {} остановилась!'.format(self.name))

    def turn(self, direction):
        print('Машина {} повернула {}!'.format(self.name, direction))




car1 = TownCar(120, 'blue', 'BMW')
car1.go()
car1.turn('налево')
car1.stop()

car2 = WorkCar(90, 'red', 'Камаз')
car2.go()
car2.turn('направо')
car2.stop()
