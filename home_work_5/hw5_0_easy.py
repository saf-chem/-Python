# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


import os
import re


def make_dir(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('{} - уже существует'.format(name))


def del_dir(name):
    try:
        os.rmdir(name)
    except FileNotFoundError:
        print('{} - папки не существует'.format(name))


if __name__ == '__main__':
    dir_name = range(1, 10)
    answer = ''
    while True:
        answer = input('Выберите пункт меню:\n'
                       '1. Создать папки dir_1 - dir_9\n'
                       '2. Удалить папки dir_1 - dir_9\n'
                       '3. Выход\n')
        if answer == '3':
            break
        elif answer == '1':
            for i in dir_name:
                make_dir('dir_' + str(i))
        elif answer == '2':
            for i in dir_name:
                del_dir('dir_' + str(i))
