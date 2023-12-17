"""
В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный)
 имеет следующие атрибуты:

Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая)
Возраст (целое положительное число) Сотрудники имеют также уникальный идентификационный номер (ID),
 который должен быть шестизначным положительным целым числом.

Ваша задача:

Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях
(Фамилия, Имя, Отчество, Возраст). Класс должен проверять валидность входных данных
и генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.

Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID).
 Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.

Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.

Добавить метод get_level в класс Employee, который будет возвращать уровень
сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).

Создать несколько объектов класса Person и Employee с разными данными и проверить,
что исключения работают корректно при передаче неверных данных.
"""


class InvalidNameError(Exception):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f"Invalid name: {self.val}. Name should be a non-empty string."


class InvalidAgeError(Exception):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f"Invalid age: {self.val}. Age should be a positive integer."


class InvalidIdError(Exception):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f"Invalid id: {self.val}. Id should be a 6-digit positive integer between 100000 and 999999."


class Person:
    def __init__(self, second_name, name, fird_name, age):
        self.second_name = self.str_validator(second_name)
        self.name = self.str_validator(name)
        self.fird_name = self.str_validator(fird_name)
        self.age = self.num_validator(age)

    @staticmethod
    def str_validator(text):
        if type(text) != str:
            raise InvalidNameError(text)
        elif len(text) == 0:
            raise InvalidNameError(text)
        return text

    @staticmethod
    def num_validator(num):
        if type(num) != int:
            raise InvalidAgeError(num)
        elif num < 0:
            raise InvalidAgeError(num)
        return num

    def __str__(self):
        return f'second_name = {self.second_name}, name = {self.name}, ' \
               f'fird_name = {self.fird_name}, age = {self.age}'

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


class Employee(Person):
    list_id = []

    def __init__(self, second_name, name, fird_name, age, person_id):
        if Person.num_validator(person_id):
            if len(list(str(person_id))) != 6:
                raise InvalidIdError(person_id)
            else:
                if person_id not in Employee.list_id:
                    super().__init__(second_name, name, fird_name, age)
                    self.person_id = person_id
                    Employee.list_id.append(person_id)
                else:
                    raise InvalidIdError(person_id)

    def get_level(self):
        return sum(int(digit) for digit in str(self.person_id)) % 7

    def __str__(self):
        return f'second_name = {self.second_name}, name = {self.name}, ' \
               f'fird_name = {self.fird_name}, age = {self.age}, person_id = {self.person_id}'


a = Person("ff", "ff", 'ff', 23)
b = Employee("fffff", "fffff", 'fffff', 23, 777777)
c = Employee("fffff", "fffff", 'fffff', 23, 777772)
print(a)
print(b)
print(c)
print(c.get_level())
