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


def rename_files(desired_name='', num_digits=0, source_ext="", target_ext="", origin_name_d=[]):
    folder = 'test_folder'
    path = os.path.join(os.getcwd(), folder)

    #     os.mkdir(path)
    count = 1
    new_name = ''
    if not os.path.exists(path):
        print('директории нет')
    else:
        for file in os.listdir(path):
            # print(file)
            ext = os.path.splitext(file)[1].lower().replace('.', '')
            old_file_name = os.path.splitext(file)[0].lower()
            # print(old_file_name, ext, source_ext)
            if ext == source_ext:
                str_num = '0' * (num_digits - len(str(count))) + str(count)
                # print(str_num)
                if origin_name_d:
                    new_name = old_file_name[origin_name_d[0]:origin_name_d[1]] \
                               + desired_name + str_num + '.' + target_ext
                    # print(new_name)
                else:
                    new_name = old_file_name[:] \
                               + desired_name + str_num + '.' + target_ext
                count += 1
                # print(new_name)
            if not os.path.exists(os.path.join(path, file)):
                os.rename(os.path.join(path, file), os.path.join(path, new_name))
            else:
                print('файл существует')


rename_files(desired_name="rrr", num_digits=2, source_ext="doc", target_ext="txt", origin_name_d=[3, 7])
