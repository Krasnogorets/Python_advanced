"""
Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

Пример использования.
На входе:


file_path = "C:/Users/User/Documents/example.txt"

На выходе:


('C:/Users/User/Documents/', 'example', '.txt')
"""


def get_file_info(file_path):
    *a, b = file_path.split("/")
    if len(a) > 1:
        a = "/".join(a) + "/"
    elif len(a) == 0:
        a = ''
    else:
        a = "/".join(a) + "/"
    *c, d = b.split(".")
    if len(c) >= 2:
        c = ".".join(c)
    elif len(c) == 1:
        c = c[0]
    elif len(c) == 0:
        c = ''
    return a, c, '.' + d


# print(get_file_info(file_path))


print(get_file_info(file_path='C:/Users/User/Documents/example.txt'))
print(get_file_info(file_path='/home/user/data/file'))
print(get_file_info(file_path='D:/myfile.txt'))
print(get_file_info(file_path='C:/Projects/project1/code/script.py'))
print(get_file_info(file_path='/home/user/docs/my.file.with.dots.txt'))
print(get_file_info(file_path='file_in_current_directory.txt'))