"""
Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""


def key_params(**kwargs):
    res = {}
    for k, v in kwargs.items():
        try:
            hash(v)
        except TypeError:
            res[str(v)] = k
        else:
            res[v] = k
    return res

# неверное решение от автотеста, выпадает в ошибку
# def key_params(**kwargs):
#     result = {}
#     for key, value in kwargs.items():
#         result[value if hash(value) else str(value)] = key
#     return result


# params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
params = key_params(name='Alice', age=30, scores=[85, 90, 78], info={'city': 'New York', 'email': 'alice@example.com'})
print(params)
