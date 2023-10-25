"""
Дан список повторяющихся элементов lst.
Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
"""
lst = [1, 2, 3, 4, 5]
# lst = [1, 1, 1, 1, 1]
# lst = [1, 1, 2, 2, 3, 3]
dct = {}
for item in lst:
    dct[item] = dct.get(item, 0) + 1
    if dct.get(item) > 2:
        dct.pop(item)
new_lst = [el for el in dct if dct[el] == 2]
print(new_lst)
