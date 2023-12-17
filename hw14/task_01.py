"""
Возьмите задачу Rectangle с прошлых семинаров. Напишите тесты для этой задачи.
Исходный код в редакторе кода надо доработать, чтобы вызывалось исключение NegativeValueError.

Используйте модуль doctest.

Тесты:

test_width: Тестирование инициализации ширины. Созданы прямоугольники r1 с шириной 5 и r4 с отрицательной шириной (-2).
 Убедимся, что r1.width корректно установлен на 5, а создание r4 вызывает исключение NegativeValueError
 с текстом Ширина должна быть положительной, а не {value}

test_height: Тестирование инициализации ширины и высоты. Созданы прямоугольники r2 с шириной 3 и высотой 4.
Проверяем, что r2.width равно 3 и r2.height равно 4.
При необходимости выбрасывать исклчение NegativeValueError с текстом Высота должна быть положительной, а не {value}

test_perimeter: Тестирование вычисления периметра. Создан прямоугольник r1 с шириной 5 и проверяем, что r1.perimeter()
 возвращает 20. Также создан прямоугольник r2 с шириной 3 и высотой 4 и проверяем, что r2.perimeter() возвращает 14.

test_area: Тестирование вычисления площади. Создан прямоугольник r1 с шириной 5 и проверяем, что r1.area()
возвращает 25. Также создан прямоугольник r2 с шириной 3 и высотой 4 и проверяем, что r2.area() возвращает 12.

test_addition: Тестирование операции сложения. Созданы прямоугольники r1 с шириной 5 и r2 с шириной 3 и высотой 4.
 Выполняем операцию сложения r1 + r2 и проверяем, что полученный прямоугольник r3 имеет правильные значения ширины
 и высоты (8 и 6.0 соответственно).

test_subtraction: Тестирование операции вычитания. Созданы прямоугольники r1 с шириной 5 и r2 с шириной 3 и высотой 4.
 Выполняем операцию вычитания r1 - r2 и проверяем, что полученный прямоугольник r3 имеет правильные значения ширины
 и высоты (2 и 2.0 соответственно).

Запускать тесты не надо, автотест это сделает сам:
"""
import doctest


class NegativeValueError(ValueError):
    pass
    # def __init__(self, value):
    #     print(f'Ширина должна быть положительной, а не {value}')


class Rectangle:
    """
    Класс, представляющий прямоугольник.

    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника

    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников
    - __eq__(other): определяет операцию "равно" для двух прямоугольников
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
    - __str__(): возвращает строковое представление прямоугольника
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
    """

    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника
        """
        return self.width * self.height

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, float(height))

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, float(height))

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self.width}, {self.height})"


def test_width(value):
    """Тестирование инициализации ширины. Созданы прямоугольники r1 с шириной 5 и r4 с отрицательной шириной (-2).
 Убедимся, что r1.width корректно установлен на 5, а создание r4 вызывает исключение NegativeValueError
 с текстом Ширина должна быть положительной, а не {value}
    >>> test_width(5)
    5
    >>> test_width(-2)
    Traceback (most recent call last):
        ...
    NegativeValueError: Ширина должна быть положительной, а не -2
    """
    if value > 0:
        r1 = Rectangle(value)
        print(r1.width)
    else:
        raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')


def test_height(width, height=None):
    """Тестирование инициализации ширины и высоты. Созданы прямоугольники r2 с шириной 3 и высотой 4.
Проверяем, что r2.width равно 3 и r2.height равно 4.
При необходимости выбрасывать исклчение NegativeValueError с текстом Высота должна быть положительной, а не {value}
    >>> test_height(3,4)
    3
    4
    >>> test_height(4,-2)
    Traceback (most recent call last):
        ...
    NegativeValueError: Высота должна быть положительной, а не -2
    """
    if height > 0:
        r2 = Rectangle(width, height)
        print(r2.width)
        print(r2.height)
    else:
        raise NegativeValueError(f'Высота должна быть положительной, а не {height}')


def test_perimeter(width, height=None):
    """Тестирование вычисления периметра. Создан прямоугольник r1 с шириной 5 и проверяем, что r1.perimeter()
 возвращает 20. Также создан прямоугольник r2 с шириной 3 и высотой 4 и проверяем, что r2.perimeter() возвращает 14.
    >>> test_perimeter(5)
    20
    >>> test_perimeter(3,4)
    14
    """
    r1 = Rectangle(width, height)
    print(r1.perimeter())


def test_area(width, height=None):
    """Тестирование вычисления площади. Создан прямоугольник r1 с шириной 5 и проверяем, что r1.area()
возвращает 25. Также создан прямоугольник r2 с шириной 3 и высотой 4 и проверяем, что r2.area() возвращает 12.
    >>> test_area(5)
    25
    >>> test_area(3,4)
    12
    """
    r1 = Rectangle(width, height)
    print(r1.area())


def test_addition():
    """Тестирование операции сложения. Созданы прямоугольники r1 с шириной 5 и r2 с шириной 3 и высотой 4.
 Выполняем операцию сложения r1 + r2 и проверяем, что полученный прямоугольник r3 имеет правильные значения ширины
 и высоты (8 и 6.0 соответственно).
    >>> r1 = Rectangle(5)
    >>> r2 = Rectangle(3,4)
    >>> r3 = Rectangle.__add__(r1,r2)
    >>> r3.width
    8
    >>> r3.height
    6.0
    """


def test_subtraction():
    """тестирование операции вычитания. Созданы прямоугольники r1 с шириной 5 и r2 с шириной 3 и высотой 4.
 Выполняем операцию вычитания r1 - r2 и проверяем, что полученный прямоугольник r3 имеет правильные значения ширины
 и высоты (2 и 2.0 соответственно).
    >>> r1 = Rectangle(5)
    >>> r2 = Rectangle(3,4)
    >>> r3 = Rectangle.__sub__(r1,r2)
    >>> r3.width
    2
    >>> r3.height
    2.0
    """


if __name__ == '__main__':
    doctest.testmod(verbose=True)

"""
Ожидаемый ответ:

**********************************************************************
, in __main__.Rectangle.__add__
Failed example:
    r3.height
Expected:
    6.0
Got:
    9.0
**********************************************************************
, in __main__.Rectangle.__sub__
Failed example:
    r3.height
Expected:
    2.0
Got:
    1.0
**********************************************************************
2 items had failures:
   1 of   5 in __main__.Rectangle.__add__
   1 of   5 in __main__.Rectangle.__sub__
***Test Failed*** 2 failures.

Ваш ответ:

**********************************************************************
, in __main__.test_addition
Failed example:
    r3.height
Expected:
    6.0
Got:
    9.0
**********************************************************************
, in __main__.test_subtraction
Failed example:
    r3.height
Expected:
    2.0
Got:
    1.0
**********************************************************************
2 items had failures:
   1 of   5 in __main__.test_addition
   1 of   5 in __main__.test_subtraction
***Test Failed*** 2 failures.
 

Скрыть терминал


"""
"""
import doctest

class NegativeValueError(ValueError):
    pass

class Rectangle:

    def __init__(self, width, height=None):
        '''
        >>> r1 = Rectangle(5)
        >>> r1.width
        5
        >>> r1.height
        5
        >>> r2 = Rectangle(3, 4)
        >>> r2.width
        3
        >>> r2.height
        4
        >>> r3 = Rectangle(-2)
        Traceback (most recent call last):
        ...
        NegativeValueError: Ширина должна быть положительной, а не -2
        >>> r4 = Rectangle(5, -3)
        Traceback (most recent call last):
        ...
        NegativeValueError: Высота должна быть положительной, а не -3
        '''
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        '''
        >>> r1 = Rectangle(5)
        >>> r1.perimeter()
        20
        >>> r2 = Rectangle(3, 4)
        >>> r2.perimeter()
        14
        '''
        return 2 * (self._width + self._height)

    def area(self):
        '''
        >>> r1 = Rectangle(5)
        >>> r1.area()
        25
        >>> r2 = Rectangle(3, 4)
        >>> r2.area()
        12
        '''
        return self._width * self._height

    def __add__(self, other):
        '''
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 + r2
        >>> r3.width
        8
        >>> r3.height
        6.0
        '''
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        '''
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 - r2
        >>> r3.width
        2
        >>> r3.height
        2.0
        '''
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)
"""