# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


import shutil
import os
name_file = os.path.realpath(__file__)
new_file = name_file +'.copy'
if not os.path.isfile(new_file):
    shutil.copy(name_file, new_file)
else:
    print('Файл уже скопирован')