#Рахматуллин Камиль БВТ2403
#Лабораторная работа №3

#Задание 1

def readWhole(file):
    with open(file, 'r') as file:
        content = file.read()
        print(content)

def readByLines(file):
    with open(file, 'r') as file:
        for line in file:
            print(line)

def optionRead(file):
    readType = str(input('Тип чтения(1: Целиком, 2: По строкам):  '))
    while (True):
        if readType == '1':
            readWhole(file)
            break
        elif readType == '2':
            readByLines(file)
            break
        else:
            readType = str(input('Введите 1(Чтение целиком) или 2(Чтение по строкам):  '))

optionRead('example.txt')

#Задание 2

userText = str(input('Ваш Текст: '))
file = open('user_input.txt', 'a')
file.write(userText + '/n')

#Задание 3

def optionRead2(file):
    try:
        f = open(file, 'r')
    except FileNotFoundError: 
        print('Файл не найден.')
    else:
        readType = str(input('Тип чтения(1: Целиком, 2: По строкам):  '))
        while (True):
            if readType == '1':
                readWhole(file)
                break
            elif readType == '2':
                readByLines(file)
                break
            else:
                readType = str(input('Введите 1(Чтение целиком) или 2(Чтение по строкам):  '))

optionRead2('example.txt')
optionRead2('non_existing_file.jpeg')