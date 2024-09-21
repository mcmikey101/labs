# Рахматуллин Камиль БВТ2403
# Лабораторная Работа №1

# Задание 1

num = int(input("Число: "))
for i in range(1, num + 1):
    print(i)

# Задание 2

num1 = int(input("Число 1: "))
num2 = int(input("Число 2: "))

if num1 != num2:
    print("Большее число: ", max(num1, num2))
else:
    print('Они равны')
