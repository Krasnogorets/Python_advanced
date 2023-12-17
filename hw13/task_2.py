"""
Допишите в вашу задачу Archive обработку исключений.

Добавьте исключение в ваш код InvalidTextError, которые будет вызываться,
 когда текст не является строкой или является пустой строкой.

И InvalidNumberError, которое будет вызываться, если число не является положительным целым числом или числом
с плавающей запятой.

archive_instance = Archive("Sample text", 42.5)
print(archive_instance)
Text is Sample text and number is 42.5. Also [] and []
Text is Sample text and number is 42.5. Also [] and []


__main__.InvalidTextError: Invalid text: . Text should be a non-empty string.
                           Invalid text: . Text should be a non-empty string.
"""
from typing import Union


class InvalidTextError(Exception):
    pass
    # def __init__(self, value):
    #     print(f'{object.__name__}: Invalid text: {value}. Text should be a non-empty string.')


class InvalidNumberError(Exception):
    pass
    # def __init__(self, value):
    #     print(f'Invalid number: {value}. Number should be a positive integer or float.')


class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        try:
            len(text)
        except InvalidTextError:
            print(f'Invalid text: {text}. Text should be a non-empty string.')
        else:
            if len(text) == 0:
                raise InvalidTextError(f'Invalid text: {text}. Text should be a non-empty string.')
        try:
            self.text = str(text)
        except InvalidTextError:
            print(f'Invalid text: {text}. Text should be a non-empty string.')
        if int(number) or float(number):
            if number < 0:
                raise InvalidNumberError(f'Invalid number: {number}. Number should be a positive integer or float.')
            else:
                self.number = number
        else:
            raise InvalidNumberError(f'Invalid number: {number}. Number should be a positive integer or float.')

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'


# Введите ваше решение ниже
archive_instance = Archive("Sample text", 42.5)
print(archive_instance)
invalid_archive_instance = Archive("", -5)
print(invalid_archive_instance)
invalid_archive_instance = Archive(5, -5)
print(invalid_archive_instance)
