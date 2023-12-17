"""
Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:

a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории

rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc, new_file_006.doc,
new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc

"""
import os

import os
import shutil

# Создать тестовую папку
folder_name = "test_folder"
folder_path = os.path.join(os.getcwd(), folder_name)
if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
os.makedirs(folder_path)

# # Заполнить тестовую папку
file_name = "test1.txt"
file_path = os.path.join(folder_path, file_name)
with open(file_path, "w") as file:
    file.write("This is a test file.\n")
    file.close()

# Заполнить тестовую папку
for i in range(10):

    file_name = f"test{i}.txt"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "w") as file:
        file.write("This is a test file.\n")
        file.close()

file_name = "test.doc"
file_path = os.path.join(folder_path, file_name)

with open(file_path, "w") as file:
    file.write("This is a test file.\n")
    file.close()


def rename_files(desired_name='', num_digits=0, source_ext="", target_ext="", origin_name_d=[]):
    folder = 'test_folder'
    path = os.path.join(os.getcwd(), folder)
    count = 1
    new_name = ''
    # if not os.path.exists(path):
    #     print('директории нет')
    # else:
    for file in os.listdir(path):
        # print(file)
        ext = os.path.splitext(file)[1].lower().replace('.', '')
        old_file_name = os.path.splitext(file)[0].lower()
        # print(old_file_name, ext, source_ext)
        if ext == source_ext:
            str_num = '0' * (num_digits - len(str(count))) + str(count)
            # print(str_num)
            # if origin_name_d:
            #     new_name = old_file_name[origin_name_d[0]:origin_name_d[1]] \
            #                + desired_name + str_num + '.' + target_ext
            #     # print(new_name)
            # else:
            new_name = desired_name + str_num + '.' + target_ext
            count += 1
            # print(new_name)
            # if not os.path.exists(os.path.join(path, file)):
            os.rename(os.path.join(path, file), os.path.join(path, new_name))
        # else:
        # print('файл существует')
    # print(*os.listdir(path))


# rename_files(desired_name="file_", num_digits=4, source_ext="txt", target_ext="txt")
# rename_files(desired_name="rrr", num_digits=2, source_ext="doc", target_ext="txt", origin_name_d=[3, 7])
rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")

