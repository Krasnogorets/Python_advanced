import os
import csv
import pickle
import json

"""
Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно обходит эту директорию
и все вложенные директории. Результаты обхода должны быть сохранены в нескольких форматах: JSON, CSV и Pickle.
Каждый результат должен содержать следующую информацию:
Путь к файлу или директории: Абсолютный путь к файлу или директории.
Тип объекта: Это файл или директория. Размер: Для файлов - размер в байтах,
 для директорий - размер, учитывая все вложенные файлы и директории в байтах.
 Важные детали:
Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.
Для файлов сохраните их размер в байтах.
Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся внутри данной директории,
и вложенных директорий.
Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.
Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.
Для обхода файловой системы вы можете использовать модуль os.
Вам необходимо написать функцию traverse_directory(directory),
которая будет выполнять обход директории и возвращать результаты в виде списка словарей.
После этого результаты должны быть сохранены в трех различных файлах (JSON, CSV и Pickle)
 с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.
"""

"""
Ожидаемый ответ:

[{'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457}, 
{'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21}, 
{'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079}, 
{'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9}, 
{'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21}, 
{'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85}, 
{'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 684}, 
{'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 342}, 
{'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171}, 
{'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101}, 
{'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}]

Ожидаемый ответ:

[{'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 342}, 
{'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171}, 
{'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101}, 
{'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}]

Ожидаемый ответ:

[{'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457}, 
{'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21}, 
{'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079}, 
{'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9}, 
{'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21}, 
{'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85}, 
{'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 684}, 
{'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 342}, 
{'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171},
{'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101}, 
{'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}]


"""



def traverse_directory(direct):
    new_list = []

    for (address, dirs, files) in os.walk(direct):
        for name in dirs:
            new_dict = {'Path': os.path.join(address, name), 'Type': 'Directory',
                        'Size': os.path.getsize(os.path.join(address, name))}
            new_list.append(new_dict)
        for name in files:
            new_dict = {'Path': os.path.join(address, name), 'Type': 'File',
                        'Size': os.path.getsize(os.path.join(address, name))}
            new_list.append(new_dict)

    print(new_list)
    save_results_to_json(new_list)
    save_results_to_csv(new_list)
    save_results_to_pickle(new_list)


def save_results_to_json(b):
    with open('hw8.json', 'w', encoding='utf-8') as f:
        json.dump(b, f, ensure_ascii=False, indent=2)


def save_results_to_csv(b):
    with open('hw8.csv', 'w', encoding='utf-8', newline='') as csv_f:
        header = b[0].keys()
        csv.writer = csv.DictWriter(csv_f, fieldnames=header)
        csv.writer.writeheader()
        csv.writer.writerows(b)


def save_results_to_pickle(b):
    with open('hw8.pickle', 'wb') as w:
        pickle.dump(b, w, protocol=pickle.DEFAULT_PROTOCOL)


# path = 'D:\ОБУЧЕНИЕ GEEKBRAINS\Погружение в Python\HW'
path = 'D:\ОБУЧЕНИЕ GEEKBRAINS\Погружение в Python\HW\mar_lander'
path2 = os.getcwd()
traverse_directory(path)
# traverse_directory(os.getcwd())


import os
import json
import csv
import pickle


def get_dir_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
        for d in dirnames:
            dp = os.path.join(dirpath, d)
            total_size += get_dir_size(dp)
    return total_size


def save_results_to_json(results, file_name):
    with open(file_name, 'w') as f:
        json.dump(results, f)


def save_results_to_csv(results, file_name):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Path', 'Type', 'Size'])
        for result in results:
            writer.writerow([result['Path'], result['Type'], result['Size']])


def save_results_to_pickle(results, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(results, f)


def traverse_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            results.append({'Path': path, 'Type': 'File', 'Size': size})
        for name in dirs:
            path = os.path.join(root, name)
            size = get_dir_size(path)
            results.append({'Path': path, 'Type': 'Directory', 'Size': size})
    return results
