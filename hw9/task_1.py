"""
Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в каждой строке,
 от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:

file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения
вида ax^2 + bx + c = 0. Функция принимает три аргумента:

a, b, c (целые числа) - коэффициенты квадратного уравнения.

Функция возвращает:
None, если уравнение не имеет корней (дискриминант отрицателен).
Одно число, если уравнение имеет один корень (дискриминант равен нулю).
Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots.
Декоратор выполняет следующие действия:
Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит
параметры a, b, c и результаты вычислений.
Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json
будет сохранена информация о параметрах и результатах вычислений для каждой строки данных из CSV-файла.
"""
import csv
import json
import math
import random


def save_to_json(num):
    def decorator(func):
        def wrapper(*args):
            # print(args[0])
            list1 = []
            new_dict = []
            try:
                with open(args[0], 'r', encoding='utf8') as read_csv:
                    csv_reader = csv.reader(read_csv, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
                    for line in csv_reader:
                        list1.append(line)
            except FileNotFoundError:
                print('file not found')
            for line in list1:
                new_dict.append({'a': line[0],
                                 'b': line[1],
                                 'c': line[2],
                                 'result': func(line[0], line[1], line[2])})

            with open('results.json', 'w', encoding='utf8') as f_write:
                json.dump(new_dict, f_write, indent=2, ensure_ascii=False)

        return wrapper

    return decorator


@save_to_json(0)
def find_roots(a, b, c):
    d = b ** 2 - (4 * a * c)
    # x1 = None
    if a == 0:
        return None
    if d > 0:
        x1 = (-1 * b + math.sqrt(d)) / (2 * a)
        x2 = (-1 * b - math.sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        x1 = (-1 * b) / (2 * a)
        return x1
    elif d < 0:
        return None


def generate_csv_file(file_name, rows):
    with open(file_name, 'w', encoding='utf-8', newline='') as csv_f:
        csv_writer = csv.writer(csv_f)
        for _ in range(rows):
            line = random.randint(-100, 100), random.randint(-200, 200), random.randint(-200, 200)
            csv_writer.writerow(line)



generate_csv_file("input_data.csv", 101)
find_roots('input_data.csv')

with open("results.json", 'r') as f:
    data = json.load(f)
    if 100 <= len(data) <= 1000:
        print(True)
    else:
        print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")
    print(len(data) == 101)
