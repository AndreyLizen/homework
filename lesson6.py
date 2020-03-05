# class Auto:
#     def __init__(self, auto_name, auto_model, auto_year=None):
#         # атрибуты класса
#         self.auto_name = auto_name     # Public
#         self._auto_model = auto_model  # защищенная Protected
#         self.__auto_year = auto_year   # максимально защищенная переменная Private
#
#     # методы класса
#     def on_auto_start(self):
#         # print(f"Заводим автомобиль {self._auto_model}")
#
#     def on_auto_stop(self):
#         print("Останавливаем работу двигателя")


# a = Auto(1, 2, 3)
# print(a)
# print(type(a))
# print(a.auto_name)
# a.on_auto_start(78)
# a.on_auto_stop()
# a.auto_name = 1934
# print(a.auto_name)

# b = Auto("Mazda", "СX9", 2019)
# print(b.auto_name)
# print(b._auto_model)
# print(b._Auto__auto_year)  # Вызов защищенной переменной
# b.on_auto_start()

# Инкапсуляция  - степени приватности, но в применении к методам!!!

# Наследование
class Shape:
    def __init__(self, color, param_1, param_2):
        self.color = color
        self.param_1 = param_1
        self.param_2 = param_2

    def square(self):
        return self.param_1 * self.param_2


class Rectangle(Shape):
    def __init__(self, color, param_1, param_2, rectangle_p):
        super().__init__(color, param_1, param_2)
        self.rectangle_p = rectangle_p

    def get_r_p(self):
        return self.rectangle_p


class Triangle(Shape):
    def __init__(self, color, param_1, param_2, triangle_p):
        super().__init__(color, param_1, param_2) # берет параметры родительского класса
        self.triangle_p = triangle_p

    def get_t_p(self):
        return self.triangle_p

r = Rectangle("white", 10, 20, True)
print(r.color)
print(r.square())
print(r.get_r_p())
t = Triangle("red", 30, 40, False)
print(t.color)
print(t.square())
print(t.get_t_p())

# полиморфизм - переопределение методов при одинаковом названии
# класс Transport
class Transport:
    def show_info(self):
        print("Родительский метод класса Transport")


# класс Auto, наследующий Transport
class Auto(Transport):
    def show_info(self):
        print("Родительский метод класса Auto")


# класс Bus, наследующий Transport
class Bus(Transport):
    def show_info(self):
        print("Родительский метод класса Bus")

t = Transport()
t.show_info()

a = Auto()
a.show_info()

b = Bus()
b.show_info()

# Домашнее задание
# 1) import time 
# time.sleep(5) # ждать 5 сек
# модуль color
# 2)
# class Transport:
#     def __init__(self, n_1, n_2):
#         S_1 = {1: n_1, 2: n_2}
#
#     def show_info(self):
#         print("Родительский метод класса Transport")

# https://en.wikipedia.org/wiki/ANSI_escape_code 
# Example of use in shell scripting