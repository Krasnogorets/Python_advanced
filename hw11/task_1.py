"""
Разработайте программное обеспечение для ведения журнала событий.
Вам необходимо создать класс, который будет представлять строки журнала и включать в себя информацию об авторе
и времени создания каждой записи.

Условие задачи:

Создайте класс MyStr, который наследуется от встроенного класса str и добавлять дополнительную информацию
о создателе строки и времени ее создания. Этот класс будет представлять строки с информацией о событиях.

Класс MyStr должен иметь следующие атрибуты и методы:

value (str): Строковое значение с описанием события.
author (str): Имя автора, создавшего запись.
time: Время создания записи в формате '%Y-%m-%d %H:%M'.

Магические методы (Dunder-методы):

Реализуйте метод __new__(cls, value, author), который создает новый объект класса MyStr с заданным value и author.
 Метод также автоматически фиксирует время создания записи.
 В этом методе создается новый объект MyStr с указанными атрибутами и текущим временем в атрибуте time.

Реализуйте метод __str__(self), который возвращает строковое представление объекта класса MyStr
с информацией о событии, авторе и времени создания.

Реализуйте метод __repr__(self), который возвращает строковое представление объекта класса MyStr.
Метод __repr__ возвращает строку, которая может быть использована для создания точно такого же объекта MyStr с теми же
значениями value и author`.

Пример использования.
Завершилось тестирование (Автор: John, Время создания: [ в формате '%Y-%m-%d %H:%M'])


Пример текста (Автор: Иван, Время создания: 2023-10-10 15:56)
Пример текста (Автор: Иван, Время создания: 2023-11-28 19:07)

MyStr('Мама мыла раму', 'Маршак')
MyStr('Мама мыла раму', 'Маршак')
"""

import time


class MyStr(str):
    value = None
    author = None
    time = None

    def __new__(cls, value, author):
        instance = super().__new__(cls)
        instance.value = value
        instance.author = author
        instance.time = time.strftime('%Y-%m-%d %H:%M')
        return instance

    def __str__(self):
        return f'{self.value} (Автор: {self.author}, Время создания: {self.time})'

    def __repr__(self):
        return f'MyStr(\'{self.value}\', \'{self.author}\')'


event = MyStr("Завершилось тестирование", "John")
print(repr(event))

my_string = MyStr("Пример текста", "Иван")
print(my_string)

my_string = MyStr("Мама мыла раму", "Маршак")
print(repr(my_string))