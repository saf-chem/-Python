# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Toys:
    def __init__(self, name, color, model):
        self.name = name
        self.color = color
        self.model = model
        self._materials()
        self._sewing()
        self._painting()

    def _materials(self):
        print(f'Закупка сырья для {self.name}')

    def _sewing(self):
        print(f'Пошив {self.name}')

    def _painting(self):
        print(f'Окраска {self.name} в {self.color}')


class CarToy:
    def production():
        print(f'Создана машинка')


class SoftToy:
    def production(self):
        print(f'Создана мягкая игрушка')


class Factory(Toys):
    def __init__(self, name, color, model):
        super().__init__(name, color, model)
        if self.model == "car":
            CarToy.production()
        if self.model == 'soft_toy':
            SoftToy().production()


toy1 = Factory('toy', 'red', 'car')
toy2 = Factory('toy', 'red', 'soft_toy')
