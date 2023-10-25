"""
У вас есть банковская карта с начальным балансом равным 0 у.е. Вы хотите управлять этой картой,
 выполняя следующие операции, для выполнения которых необходимо написать следующие функции:

check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
deposit(amount): Пополнение счёта.
withdraw(amount): Снятие денег.
exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.

Пополнение счета:

Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму.
Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY.
Если сумма пополнения превышает RICHNESS_SUM, то начисляется налог на богатство в размере RICHNESS_PERCENT процентов.

Снятие средств:

Функция withdraw(amount) позволяет клиенту снимать средства со счета.
Сумма снятия также должна быть кратной MULTIPLICITY.
При снятии средств начисляется комиссия в процентах от снимаемой суммы,
которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.

Завершение работы:

Функция exit() завершает работу с банковским счетом.
Перед завершением, если на счету больше RICHNESS_SUM, начисляется налог на богатство в размере RICHNESS_PERCENT процентов.

Проверка кратности суммы:

Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному множителю MULTIPLICITY.
Реализуйте программу для управления банковским счетом, используя библиотеку decimal для точных вычислений.


Пример

На входе:


deposit(1000)
withdraw(200)
exit()

print(operations)
На выходе:


['Пополнение карты на 1000 у.е. Итого 1000 у.е.', 'Снятие с карты True у.е. П
"""
# import decimal
#
# MULTIPLICITY: decimal = 50
# RICHNESS_PERCENT: decimal = 0.1
# RICHNESS_SUM: decimal = 2000
# amount: int = 0
# MIN_REMOVAL: decimal = 200
# MAX_REMOVAL: decimal = 500
# operations = []
#
#
# def check_multiplicity(x: decimal):
#     if x % MULTIPLICITY == 0:
#         return True
#     return False
#
#
# def deposit(x: decimal):
#     global amount, operations
#     if check_multiplicity(x):
#         amount += x
#         if amount > RICHNESS_SUM:
#             amount -= round(amount * RICHNESS_PERCENT)
#     else:
#         print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
#     operations.append(f'Пополнение карты на {x} у.е. Итого {amount} у.е.')
#
#
# def withdraw(x: decimal):
#     global amount
#     if check_multiplicity(x):
#         if x <= MIN_REMOVAL:
#             y: decimal = 0.15
#             amount -= round(x + x * y)
#         elif MIN_REMOVAL < x <= MAX_REMOVAL:
#             y: decimal = 0.10
#             amount -= round(x + x * y)
#         else:
#             y: decimal = 0.05
#             amount -= round(x + x * y)
#     else:
#         print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
#     operations.append(f'Снятие с карты {check_multiplicity(x)} у.е. '
#                       f'Процент за снятие {round(x * y)}. Итого {amount} у.е.')
#
#
# def exit():
#     global amount
#     if amount > RICHNESS_SUM:
#         amount -= round(amount * RICHNESS_PERCENT)
#     operations.append(f'Возьмите карту на которой {amount} у.е.')
#     print(operations)
import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []


def check_multiplicity(amount):
    """Проверка кратности суммы"""
    if (amount % MULTIPLICITY) != 0:
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
        return False
    return True


def deposit(amount):
    """Пополнение счёта"""
    global bank_account, count
    if not check_multiplicity(amount):
        return False  # Операция не выполнена из-за некратной суммы
    count += 1
    bank_account += amount
    operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')
    return True


def withdraw(amount):
    """Снятие денег"""
    global bank_account, count
    amount = check_multiplicity(amount)
    percent = amount * PERCENT_REMOVAL
    percent = MIN_REMOVAL if percent < MIN_REMOVAL else MAX_REMOVAL if percent > MAX_REMOVAL else percent
    if bank_account >= amount + percent:
        count += 1
        bank_account = bank_account - amount - percent
        operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {percent}. Итого {bank_account} у.е.')
    else:
        operations.append(
            f'Недостаточно средств. Сумма с комиссией {amount + percent} у.е. На карте {bank_account} у.е.')


def exit():
    """Завершение работы"""
    global bank_account, operations
    if bank_account > RICHNESS_SUM:
        percent = bank_account * RICHNESS_PERCENT
        bank_account -= percent
        operations.append(
            f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {percent} у.е. Итого {bank_account} у.е.')
    operations.append(f'Возьмите карту на которой {bank_account} у.е.')


deposit(1000)
withdraw(200)
exit()
print(operations)
