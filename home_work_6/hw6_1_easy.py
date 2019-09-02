# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print('Машина {} поехала!'.format(self.name))

    def stop(self):
        print('Машина {} остановилась!'.format(self.name))

    def turn(self, direction):
        print('Машина {} повернула {}!'.format(self.name, direction))


class PoliceCar(Car):
    def __init__(self, is_police=True):
        super().__init__(is_police)


class WorkCar(Car):
    pass


class SportCar(Car):
    pass


class TownCar(Car):
    pass


car1 = TownCar(100, 'white', 'Tata')
car1.go()
car1.turn('направо')
car1.stop()
