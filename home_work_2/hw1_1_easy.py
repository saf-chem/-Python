# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

first_list = [0, 2, 3, 'ivan', 4, 5, 9, 7, 8, 11]
second_list = ['ivan', 4, 2, 7, 9]
first_list = set(first_list)
second_list = set(second_list)
print(first_list - second_list)

