# class MyClass:
#     def __init__(self, param):
#         self.param = param
#
#     def __del__(self):
#         print(f"Удаляем объект {self.param} класса MyClass")
#
# mc = MyClass("text")
# del mc

# class MyClass1:
#     def __init__(self, param1, param2):
#         self.param1 = param1
#         self.param2 = param2
#
#     def __add__(self, other):
#         return MyClass1(self.param1 + other.param1, self.param2 + other.param2)
#
#     def __str__(self):
#         return f"Объект с параметрами {self.param1, self.param2}"
#
# my_1 = MyClass1('text1', 'text2')
# print(my_1)
#
# my1 = MyClass1(34, 22)
# my2 = MyClass1(404, 202)
# my3 = MyClass1(100, 100)
# print(my1 + my2 + my3)
#
# my1 = MyClass1("34", "22")
# my2 = MyClass1("404", "202")
# my3 = MyClass1("100", "100")
# print(my1 + my2 + my3)

# class MyClass:
#     def __setattr__(self, attr, value):
#         if attr == "width":
#             self.__dict__[attr] = value
#             print(self.__dict__)
#         else:
#             print(f"Атрибут {attr} недопустим")
#
#
# mc = MyClass()
# mc.width = 40

# class Class1:
#     def __init__(self, param):
#         self.param = param
#
#     def __str__(self):
#        return str(self.param)
#
#
# class Class2:
#     def __init__(self, *args):
#         self.my_list = []
#         for el in args:
#             self.my_list.append(Class1(el))
#
#     def __getitem__(self, index):
#         return self.my_list[index]
#
#
# my_obj = Class2(10, True, "text")
# print(my_obj.my_list[0])
# print(my_obj[1])
# print(my_obj[2])

# class MyClass:
#     def __init__(self, param):
#         self.param = param
#
#     def __call__(self, newparam):
#         self.param = newparam
#
#     def __str__(self):
#         return f"Значение параметра - {self.param};"
#
#
# obj_1 = MyClass("width")
# obj_2 = MyClass("height")
#
# obj_1("length")
# obj_2("square")
#
# print(obj_1, obj_2)

# class ParentClass:
#     def __init__(self):
#         print("Конструктор класса-родителя")
#
#     def my_method(self):
#         print("Метод my_method() класса ParentClass")
#
#
# class ChildClass(ParentClass):
#     def __init__(self):
#         print("Конструктор дочернего класса")
#         ParentClass.__init__(self)
#
#     def my_method(self):
#         print("Метод my_method() класса ChildClass")
#         ParentClass.my_method(self)
#
#
# c = ChildClass()
# c.my_method()

# from abc import ABC, abstractmethod
#
# class MyAbstractClass(ABC):
#     @abstractmethod
#     def my_method_1(self):
#         pass
#     @abstractmethod
#     def my_method_2(self):
#         pass

#
# class MyClass(MyAbstractClass):
#     def my_method_1(self):
#         print("Метод my_method_1()")
#
#     def my_method_2(self):
#         print("Метод my_method_2()")
#
# mc = MyClass()
# mc.my_method_1()
#
# # ИТЕРАТОРЫ
#
# class Iterator:
#     """
#     Объект-итератор
#     """
#     def __init__(self, start=0):
#         self.i = start
#     # У итератора есть метод __next__
#
#     def __next__(self):
#         self.i += 1
#         if self.i <= 5:
#             return self.i
#         else:
#             raise StopIteration
#
# class IterObj:
#     """
#     Объект, поддерживающий интерфейс итерации (итерируемый объект)
#     """
#     def __init__(self, start=0):
#         self.start = start - 1
#     def __iter__(self):
#         # Метод __iter__ должен возвращать объект-итератор
#         return Iterator(self.start)
#
# obj = IterObj(start=2)
# for el in obj:
#     print(el)
#
# # объединенный оператор
# class Iter:
#     def __init__(self, start=0):
#         self.i = start - 1
#
#     # Метод __iter__ должен возвращать объект-итератор
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i <= 5:
#             return self.i
#         else:
#             raise StopIteration
#
# obj = Iter(start=2)
# for el in obj:
#     print(el)

# class MyClass:
#     def __init__(self, param_1, param_2):
#         self.param_1 = param_1
#         self.param_2 = param_2
#
#     @property
#     def my_method(self):
#         return f"Параметры, переданные в класс:" \
#             f" {self.param_1}, {self.param_2}"
#
# mc = MyClass("text_1", "text_2")
#
# print(mc.param_1)
# print(mc.param_2)
#
# print(mc.my_method)


# класс Auto
# class Auto:
#
#     # конструктор класса Auto
#     def __init__(self, year):
#         # Инициализация свойств.
#         self.year = year
#
#     # создаем свойство года
#     @property
#     def year(self):
#         return self.__year
#
#     # сеттер для создания свойств - для защищенных объектов
#     @year.setter
#     def year(self, year):
#         if year < 2000:
#             self.__year = 2000
#         elif year > 2019:
#             self.__year = 2019
#         else:
#             self.__year = year
#
#     def get_auto_year(self):
#         return f"Автомобиль выпущен в {str(self.year)} году"
#
# a = Auto(2090)
# print(a.get_auto_year())

class Mat:
    def __init__(self, m):
        self.m = m
m1 = m([[1,2],[3,4]])
print(m1) - матрица
print(m1 + m2) - сумма матриц

print(m1 + m2)
print(m1 - m2) - не должно быть отрицательным
print(m1 * m2)
print(m1 / m2) - целочисленное

m1.make_ordfer(3) - делит по рядам
