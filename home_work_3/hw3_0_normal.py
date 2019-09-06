# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.


list_name = ['Павел Петров', 'Сергей Николаев', 'Анастасия Егорова']
list_salary = [500000, 10000, 22000]
tax = 0.13

name_and_salary = dict(zip(list_name, list_salary))

with open('salary.txt', 'w') as file:
    for name, salary in name_and_salary.items():
        file.writelines([name, ' - ', str(salary), '\n'])

with open('salary.txt') as file:
    for line in file.readlines():
        name, max_salary = line.strip().split(' - ')
        max_salary = int(max_salary)
        if max_salary < 500000:
            print(f'{name.upper()} - зарплата {max_salary - max_salary * tax}')