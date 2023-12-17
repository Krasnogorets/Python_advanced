"""Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров. Данная промежуточная аттестация
оценивается по системе "зачет" / "не зачет" "Зачет" ставится, если Слушатель успешно выполнил задание. "Незачет"
ставится, если Слушатель не выполнил задание. Критерии оценивания: 1 - Слушатель написал корректный код для задачи,
добавил к ним логирование ошибок и полезной информации."""
import logging
from typing import Union
import argparse


FORMAT = '{levelname:<8} - {asctime}.' \
         'в строке {lineno} функция "{funcName}()" ' \
         ' выдало сообщение: {msg}'

logging.basicConfig(filename='task_01.log',
                    encoding='utf-8', level=logging.NOTSET, format=FORMAT, style='{', datefmt='%H:%M:%S')
logger = logging.getLogger(__name__)


class InvalidTextError(Exception):
    pass


class InvalidNumberError(Exception):
    pass


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
        logger.info(
            f"программа сделала: получен запрос на создание экземплара класса Archive с аргументами{text, number}")
        try:
            len(text)
        except InvalidTextError:
            logger.error(
                f'Поймали ошибку: {InvalidNumberError} Invalid text: {text}. Text should be a non-empty string.')
            print(f'Invalid text: {text}. Text should be a non-empty string.')
        else:
            if len(text) == 0:
                logger.error(f'Поймали ошибку: {InvalidNumberError} Invalid text: {text}.'
                             f' Text should be a non-empty string.')
                raise InvalidTextError(f'Invalid text: {text}. Text should be a non-empty string.')

        try:
            self.text = str(text)
        except InvalidTextError:
            print(f'Invalid text: {text}. Text should be a non-empty string.')
            logger.error(f'Поймали ошибку: {InvalidNumberError} Invalid text: {text}.'
                         f' Text should be a non-empty string.')
        if int(number) or float(number):
            if number < 0:
                logger.error(f'Поймали ошибку: {InvalidNumberError} Invalid text: {text}.'
                             f' Text should be a non-empty string.')
                raise InvalidNumberError(f'Invalid number: {number}. Number should be a positive integer or float.')
            else:
                self.number = number
        else:
            logger.error(f'Поймали ошибку: {InvalidNumberError} Invalid text: {text}.'
                         f' Text should be a non-empty string.')
            raise InvalidNumberError(f'Invalid number: {number}. Number should be a positive integer or float.')
        logger.info(f"программа сделала: {self.__str__()}")

    def __str__(self):

        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'


def log_all():
    logger.critical('конец работы')


if __name__ == '__main__':
    log_all()
    parser = argparse.ArgumentParser(description='get Archive data')
    parser.add_argument('-text', metavar='text', type=str,
                        nargs=1, help="введите строку и вещественное число через пробел"
                                      "введение аргументов необязательно (default ='')", default='1')
    parser.add_argument('-number', metavar='number', type=float,
                        nargs=1, help="введите вещественное число, "
                                      "введение аргументов необязательно (default = 0)", default=1)
    args_1, unrecognized_args = parser.parse_known_args()

    if unrecognized_args:
        print(args_1, unrecognized_args)
        logger.error(f" Unrecognized arguments: {unrecognized_args}")
        if len(unrecognized_args)>1:
            c2 = Archive(unrecognized_args[0], float(unrecognized_args[1]))
            logger.info(f'Получили аргументы: {unrecognized_args[0]},{float(unrecognized_args[1])} ')
        else:
            c2 = Archive(str(unrecognized_args[0]), args_1.number)
            logger.info(f'Получили аргументы: {unrecognized_args[0]},{args_1.number} ')
    else:
        c2 = Archive(args_1.text, args_1.number)
    archive_instance = Archive("Sample text", 42.5)
    print(archive_instance)

