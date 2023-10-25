"""
На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
Напишите программу, которая должна возвращать сумму и произведение дробей.
Для проверки своего кода используйте модуль fractions.
"""
import fractions

frac1 = "1/2"
frac2 = "1/3"

numerator_1 = int(frac1.split('/')[0])
denominator_1 = int(frac1.split('/')[1])
numerator_2 = int(frac2.split('/')[0])
denominator_2 = int(frac2.split('/')[1])
nod = denominator_1 * denominator_2
print(f'Сумма дробей: {int(numerator_1 * (nod / denominator_1) + numerator_2 * (nod / denominator_2))}/{nod}')
print(f'Произведение дробей: {int(numerator_1 * numerator_2)}/{int(denominator_1 * denominator_2)}')
print(f'Сумма дробей: {fractions.Fraction(frac1) + fractions.Fraction(frac2)}')
print(f'Произведение дробей: {fractions.Fraction(frac1) * fractions.Fraction(frac2)}')
