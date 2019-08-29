# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os


def path_dir():
    path_dir_new = os.listdir()
    print('Папки текущей директории:')
    for index, element in enumerate(path_dir_new, start=1):
        if os.path.isdir(element):
            print('{}. {}'.format(index, element))


if __name__ == '__main__':
    path_dir()
