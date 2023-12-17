"""
Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.

Создайте файл __init__.py и запишите в него функцию rename_files
"""
import os
import shutil
#
# folder = 'package'
# path = os.path.join(os.getcwd(), folder)
# if not os.path.exists(path):
#     os.mkdir(path)
# if not os.listdir(path):
#     shutil.copy('D:\ОБУЧЕНИЕ GEEKBRAINS\Погружение в Python\семинары\sem_7_4.py', path)
#
# # if not os.listdir(path):
#     shutil.copy('task_1.py', path)
#     shutil.copy('D:\ОБУЧЕНИЕ GEEKBRAINS\Погружение в Python\семинары\sem_7_3.py', path)
# # if not os.listdir(path):
#     shutil.copy('D:\ОБУЧЕНИЕ GEEKBRAINS\Погружение в Python\семинары\sem_7_6.py', path)
# # if not os.listdir(path):
#     shutil.copy('D:\ОБУЧЕНИЕ GEEKBRAINS\Погружение в Python\семинары\sem_7_7.py', path)
# path = os.path.join(path, '__init__.py')
with open('__init__.py', 'w', encoding='utf-8') as f:
    f.writelines('def rename_files():\n')
    # f.writelines("__all__ = ['rename_files']")

# print(path)
# print(os.listdir(path))
