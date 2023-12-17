"""
Разработать класс Matrix, представляющий матрицу и обеспечивающий базовые операции с матрицами.

Атрибуты класса:

rows (int): Количество строк в матрице.
cols (int): Количество столбцов в матрице.
data (list): Двумерный список, содержащий элементы матрицы.

Методы класса:

__init__(self, rows, cols): Конструктор класса, который инициализирует атрибуты rows и cols,
а также создает двумерный список data размером rows x cols и заполняет его нулями.

__str__(self): Метод, возвращающий строковое представление матрицы.
Возвращаемая строка представляет матрицу, где элементы разделены пробелами,
 а строки разделены символами новой строки. Например:
1 2 3
4 5 6

__repr__(self): Метод, возвращающий строковое представление объекта, которое может быть использовано
для создания нового объекта того же класса с такими же размерами и данными.

__eq__(self, other): Метод, определяющий операцию "равно" для двух матриц. Сравнивает две матрицы
и возвращает True, если они имеют одинаковое количество строк и столбцов,
а также все элементы равны. Иначе возвращает False.

__add__(self, other): Метод, определяющий операцию сложения двух матриц.
Проверяет, что обе матрицы имеют одинаковые размеры (количество строк и столбцов). Если размеры совпадают,
 создает новую матрицу, где каждый элемент равен сумме соответствующих элементов входных матриц.

__mul__(self, other): Метод, определяющий операцию умножения двух матриц.
Проверяет, что количество столбцов в первой матрице равно количеству строк во второй матрице.
Если условие выполняется, создает новую матрицу, где элемент на позиции [i][j] равен сумме произведений элементов
соответствующей строки из первой матрицы и столбца из второй матрицы.
"""


class Matrix:
    rows: int = None
    cols: int = None
    data: list = []

    def __init__(self, rows, cols, data: list = None):
        self.rows = rows
        self.cols = cols
        if data is None:
            self.data = [[0 for j in range(self.cols)] for i in range(self.rows)]
        self.data = data

    def __str__(self):
        res: str = ""
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                res += f'{self.data[i][j]} '
            res = res[:-1]
            res += f'\n'
        res = res[:-1]
        return res

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    def __eq__(self, other):
        if self.rows == other.rows:
            if self.cols == other.cols:
                for i in range(self.rows):
                    for j in range(self.cols):
                        if self.data[i][j] != other.data[i][j]:
                            return False
            else:
                return False
        else:
            return False
        return True

    def __add__(self, other):
        if self.rows == other.rows:
            if self.cols == other.cols:
                new_data = [[0 for j in range(self.cols)] for i in range(self.rows)]
                for i in range(self.rows):
                    for j in range(self.cols):
                        new_data[i][j] = self.data[i][j] + other.data[i][j]
                return Matrix(self.rows, self.cols, new_data)
            else:
                return False
        else:
            return False

    def __mul__(self, other):
        new_data = list(map(lambda x: list(map(lambda y: sum(i * j for i, j in zip(x, y)),
                                               zip(*other.data))), self.data))
        return Matrix(self.rows, self.cols, new_data)


#
# matrix1 = Matrix(2, 3)
# matrix1.data = [[1, 2, 3], [4, 5, 6]]
#
# matrix2 = Matrix(2, 3)
# matrix2.data = [[7, 8, 9], [10, 11, 12]]
#
# matrix3 = Matrix(2, 4)
# matrix3.data = [[1, 2, 3, 4], [4, 5, 6, 7]]
#
# matrix4 = Matrix(2, 3)
# matrix4.data = [[1, 2, 3], [4, 5, 6]]
# # Выводим матрицы
# print(matrix1)
#
# print(matrix2)
# print(matrix1 == matrix2)
# print(matrix1 == matrix3)
# print(matrix1 == matrix4)

# Выполняем операцию сложения матриц
# matrix_sum = matrix1 + matrix2
# print(matrix_sum)

# matrix3 = Matrix(3, 2)
# matrix3.data = [[1, 2], [3, 4], [5, 6]]
#
# matrix4 = Matrix(2, 2)
# matrix4.data = [[7, 8], [9, 10]]
#
# result = matrix3 * matrix4
# print(result)

# Создаем матрицы
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)

print(matrix2)

# Сравниваем матрицы
print(matrix1 == matrix2)

# Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)

# Выполняем операцию умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)
