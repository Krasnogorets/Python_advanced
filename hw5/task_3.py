"""
Создайте функцию генератор чисел Фибоначчи fibonacci.
"""


def fibonacci(n=20):
    a = 0
    b = 1
    yield a
    for _ in range(n):
        a, b = b, a + b
        yield a


f = fibonacci()
for i in range(10):
    print(next(f))

