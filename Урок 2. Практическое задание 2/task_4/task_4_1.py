"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
"""

number = int(input("Enter number "))
sum_number = 0
n = 1
for element in range(number):
    sum_number += n
    n /= -2
    print(n)

print(sum_number)
