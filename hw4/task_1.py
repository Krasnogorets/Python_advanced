"""
Напишите функцию для транспонирования матрицы transposed_matrix,
принимает в аргументы matrix, и возвращает транспонированную матрицу.
"""

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def transpose(m):
    a = [[0 for j in range(len(m))] for i in range(len(m[0]))]
    for i in range(len(m)):
        for j in range(len(m)):
            a[i][j] = m[j][i]
    return a


print(transpose(matrix))
