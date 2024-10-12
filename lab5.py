#Рахматуллин Камиль БВТ2403
#Лабораторная работа №5

#Задание 1

class Book():
    title = 'Война и Мир'
    author = 'Лев Толстой'
    year = '1868'
    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"
    
book = Book()

print(book.get_info())

#Задание 2

class Circle():
    def __init__(self, radius):
        self.__radius = radius
        self.test = 'test'
    def get_radius(self):
        return self.__radius
    def set_radius(self, newRad):
        self.__radius = newRad

circle = Circle(4)
print(circle.get_radius())
circle.set_radius(2)
print(circle.get_radius())