"""
Разработайте программу для работы с прямоугольниками. Необходимо создать класс Rectangle,
который будет представлять прямоугольник с заданными шириной и высотой.

Атрибуты класса:
width (int): Ширина прямоугольника. height (int): Высота прямоугольника.
Методы класса:
__init__(self, width, height=None): Конструктор класса.
Принимает ширину и высоту прямоугольника. Если высота не указана (по умолчанию None),
то считается, что прямоугольник является квадратом, и высота устанавливается равной ширине.
perimeter(self): Метод для вычисления периметра прямоугольника. Возвращает целое число - значение периметра.
area(self): Метод для вычисления площади прямоугольника. Возвращает целое число - значение площади.
__add__(self, other): Магический метод, который определяет операцию сложения (+) для двух прямоугольников.
Принимает другой прямоугольник other. Создает новый прямоугольник, который представляет собой объединение исходных
прямоугольников по периметру. Возвращает новый прямоугольник.
__sub__(self, other): Магический метод, который определяет операцию вычитания (-) одного прямоугольника из другого.
 Принимает вычитаемый прямоугольник other. Создает новый прямоугольник, представляющий разницу периметров исходных
 прямоугольников, и вычисляет высоту на основе этой разницы. Возвращает новый прямоугольник.
__lt__(self, other): Магический метод, который определяет операцию "меньше" (<) для двух прямоугольников.
Принимает другой прямоугольник other. Возвращает True, если площадь первого прямоугольника меньше площади
второго, иначе False.

__eq__(self, other): Магический метод, который определяет операцию "равно" (==) для двух прямоугольников.
Принимает другой прямоугольник other. Возвращает True, если площади равны, иначе False.

__le__(self, other): Магический метод, который определяет операцию "меньше или равно" (<=) для двух прямоугольников.
 Принимает другой прямоугольник other. Возвращает True, если площадь первого прямоугольника меньше
 или равна площади второго, иначе False.

__str__(self): Магический метод, возвращающий строковое представление прямоугольника.
 Возвращает строку, описывающую ширину и высоту прямоугольника в виде:
Прямоугольник со сторонами 2 и 3,
где первое число - это ширина, а второе - высота.

__repr__(self): Магический метод, возвращающий строковое представление прямоугольника,
которое может быть использовано для создания нового объекта такого же класса с теми же атрибутами.

Пояснение:

Метод __add__ объединяет два прямоугольника по периметру и создает новый прямоугольник.
Метод __sub__ вычитает один прямоугольник из другого, представляя разницу периметров исходных прямоугольников,
 и создает новый прямоугольник.
Методы сравнения __lt__, __eq__ и __le__ сравнивают прямоугольники по их площади.
Методы __str__ и __repr__ предоставляют строковое представление объекта класса Rectangle.

Пример использования:
На входе:
rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)

print(f"Периметр rect1: {rect1.perimeter()}")
print(f"Площадь rect2: {rect2.area()}")
print(f"rect1 < rect2: {rect1 < rect2}")
print(f"rect1 == rect2: {rect1 == rect2}")
print(f"rect1 <= rect2: {rect1 <= rect2}")

rect3 = rect1 + rect2
print(f"Периметр rect3: {rect3.perimeter()}")
rect4 = rect1 - rect2
print(f"Ширина rect4: {rect4.width}")

Периметр rect1: 30
Площадь rect2: 21
rect1 < rect2: False
rect1 == rect2: False
rect1 <= rect2: False
Периметр rect3: 50
Ширина rect4: 2

Ожидаемый ответ:

Прямоугольник со сторонами 4 и 5
Прямоугольник со сторонами 3 и 3
18
20
12
9
Прямоугольник со сторонами 7 и 8
Прямоугольник со сторонами 1 и 2
False
False
False
Rectangle(4, 5)
Rectangle(3, 3)
"""


class Rectangle:
    width: int = None
    height: int = None

    def __init__(self, width: int, height: int = None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def perimeter(self) -> int:
        return 2 * (self.height + self.width)

    def area(self) -> int:
        return self.width * self.height

    def __add__(self, other):
        sum_per = self.perimeter() + other.perimeter()
        height = round(sum_per / 4)
        for i in range(height + 2):
            if (i + height) * 2 == sum_per:
                return Rectangle(i, height)

    def __sub__(self, other):
        sub_per = abs(self.perimeter() - other.perimeter())
        height = round(sub_per / 4)
        for i in range(height + 2):
            if (i + height) * 2 == sub_per:
                return Rectangle(i, height)

    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.height}'

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()


# rect1 = Rectangle(5, 10)
# rect2 = Rectangle(3, 7)
#
# print(f"Периметр rect1: {rect1.perimeter()}")
# print(f"Площадь rect2: {rect2.area()}")
# print(f"rect1 < rect2: {rect1 < rect2}")
# print(f"rect1 == rect2: {rect1 == rect2}")
# print(f"rect1 <= rect2: {rect1 <= rect2}")
#
# rect3 = rect1 + rect2
#
# print(f"Периметр rect3: {rect3.perimeter()}")
# rect4 = rect1 - rect2
# print(f"Ширина rect4: {rect4.width}")


rect1 = Rectangle(4, 5)
rect2 = Rectangle(3, 3)

print(rect1)
print(rect2)

print(rect1.perimeter())
print(rect1.area())
print(rect2.perimeter())
print(rect2.area())

rect_sum = rect1 + rect2
rect_diff = rect1 - rect2

print(rect_sum)
print(rect_diff)

print(rect1 < rect2)
print(rect1 == rect2)
print(rect1 <= rect2)

print(repr(rect1))
print(repr(rect2))
