"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""

number = int(input("Enter number "))
number_for_print = number


def calc(number, even=0, uneven=0):
    if number > 0:
        new_number = number % 10
        if new_number % 2 == 0:
            even += 1
        else:
            uneven += 1
        number = number // 10
        return calc(number, even, uneven)
    else:
        return f'В числе {number_for_print} всего {even+uneven} цифр, из которых {even} чётных и {uneven} нечётных'


f = calc(number, even=0, uneven=0)
print(f)
