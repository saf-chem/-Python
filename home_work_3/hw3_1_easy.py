# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def max_number(a, b, c):
    number_list = [a, b, c]
    max_number = (max(number_list))
    return max_number


num_1 = int(input('Введите значение первого числа: '))
num_2 = int(input('Введите значение второго числа: '))
num_3 = int(input('Введите значение третьего числа: '))

result = max_number(num_1, num_2, num_3)
print('Максимальное число из введеных вами: {}'.format(result))
