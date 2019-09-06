# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.



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


toy1 = Toys('bugs', 'blue', 'jiraf')
