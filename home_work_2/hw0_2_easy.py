# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []
for a in first_list:
    a = int(a)
    if a % 2 == 0:
        new_list.append(a/4)
    else:
        new_list.append(a*2)
print(new_list)