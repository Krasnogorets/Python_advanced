"""
Задание №4
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.

"""
from random import randint
from random import randbytes
import os

# os.mkdir('task_7_4_files')

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
sonants = ['a', 'e', 'i', 'o', 'u']


def file_creation(file_type, min_len=6, max_len=30, min_bytes=256, max_bytes=4096, files_qts=42, path_1='task_7_4_files/'):
    for _ in range(files_qts):
        file_name = path_1 + names_generator(min_len, max_len) + '.' + file_type
        with open(file_name, 'wb') as f:
            file_names = []
            for file_name in os.walk(path_1):
                file_names.append(file_name)
            if f not in file_names:
                f.write(randbytes(randint(min_bytes, max_bytes)))
            else:
                print('file exists')


def names_generator(min_len, max_len):
    c = ""
    for i in range(randint(min_len, max_len)):
        o = randint(0, 1)
        if o == 1:
            c += consonants[randint(0, 20)]
        else:
            c += sonants[randint(0, 4)]
    return c


file_creation('txt', 5, 8, 300, 2000, 40)
