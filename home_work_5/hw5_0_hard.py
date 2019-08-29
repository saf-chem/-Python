# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def change_dir():
    if not dir_name:
        print('Необходимо указать имя директории вторым параметром')
        return
    try:
        os.chdir(dir_name)
        print('Успешно перешли в папку: {}'.format(dir_name))
        print('Текущий каталог: ', os.getcwd())
    except FileNotFoundError:
        print('dir_{} - папки не существует'.format(dir_name))


def file_copy():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    current_dir = os.getcwd()
    old_file = os.path.join(current_dir, file_name)
    new_file = os.path.join(current_dir, (file_name + '.copy'))
    if not os.path.isfile(new_file):
        shutil.copy(old_file, new_file)
        print(new_file + ' - создан')
    else:
        print('Файл уже скопирован')


def del_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    curr_dir = os.getcwd()
    old_file = os.path.join(curr_dir, file_name)
    if os.path.isfile(old_file):
        answer = input('Вы уверены что хотите удалить файл? y/n: ')
        if answer == 'y':
            os.remove(old_file)
            print(old_file + ' - удален')
        else:
            return
    else:
        print('Файла не существует')


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print('cp - создает копию указанного файла')
    print('rm - удаляет указанный файл')
    print('cd - смена директории на указанную')
    print('ls - отображает полный путь текущей директории')


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def curr_dir():
    print('Текущая директория ', os.getcwd())



do = {
    'help': print_help,
    'mkdir': make_dir,
    'ping': ping,
    'cp': file_copy,
    'cd': change_dir,
    'rm': del_file,
    'ls': curr_dir
}

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
