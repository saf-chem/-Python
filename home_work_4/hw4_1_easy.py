# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.


fruit_list_1 = ['дыня', 'нектарин', 'апельсин' 'яблоко', 'мандарин', 'киви', 'груша', 'персик', 'абрикос']
fruit_list_2 = ['банан', 'киви', 'груша', 'лимон', 'яблоко', 'ананас', 'мандарин', 'дыня']

sort_list = [i for i in fruit_list_1 if i in fruit_list_2]
print(sort_list)
