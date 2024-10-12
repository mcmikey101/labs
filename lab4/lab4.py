# Рахматуллин Камиль БВТ2403
# Лабораторная Работа №4

# Задание 1

import math
import datetime

num = 4
print("Корень ", num, ' = ', math.sqrt(num))

print('Дата и Время: ', datetime.datetime.now())

#Задание 2

import my_module

print(my_module.Addition(1, 2))
print(my_module.Addition('1', 2))
print(my_module.Subtraction(5, 3))
print(my_module.Subtraction('5', 3))

#Задание 3

import package.text_module as tm
import package.number_module as nm

print(tm.toCaps('test_word'))
print(tm.toCaps(123))

print(tm.scramble('normal_word'))
print(tm.scramble(999))

print(nm.isEven(4))
print(nm.isEven(5))
print(nm.isOdd(4))
print(nm.isOdd(5))
