
# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
n = int(input('Введите размер количества элементов списка '))
new_list = []
for i in range(n):
    new_list.append(random.randint(-100, 100))
print(new_list)
