# Рахматуллин Камиль БВТ2403
# Лабораторная Работа №2

# Задание 1

def greet(name):
    print('Привет, ' + str(name) + '.')

greet('Камиль')
greet(2)
greet(True)

def square(number):
    if type(number) is int:
        return number ** 2
    else:
        return 'Не число.'
    
print(square(2))
print(square('a'))

def max_of_two(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return 'Они равны'
    
print(max_of_two(5, 10))

# Задание 2

def describe_person(name, age=30):
    print('Имя: ' + name)
    print('Возраст: ' + str(age))
    
describe_person('Камиль', 18)

# Задание 3

def is_prime(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    if prime:
        return True
    return False

print(is_prime(4))
print(is_prime(7))

