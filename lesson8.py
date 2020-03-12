# class MyClass:
#     @staticmethod
#     def on_sum_1(param_1, param_2):  # Статический метод
#         return param_1 + param_2
#
#     def on_sum_2(self, param_1, param_2):  # Обычный метод класса
#         return param_1 + param_2
#
#     def on_sum_3(self, param_1, param_2):
#         return MyClass.on_sum_1(param_1, param_2)  # Вызов статического метода
#
#
# print(MyClass.on_sum_1(20, 30))
# mc = MyClass()
# print(mc.on_sum_2(20, 10))
# print(mc.on_sum_1(40, 30))
# print(mc.on_sum_3(50, 50))


# class MyClass:
#     def __init__(self, param1):
#         MyClass.param1 = param1
#
#     @staticmethod
#     def on_sum_1(param_1):  # Статический метод
#         return True if param_1.isdigit() else False
#
#     @classmethod
#     def my_method(cls, param):  # Метод класса
#         MyClass.param1 = 90
#         print(cls, param)
#
#
# MyClass.my_method(30)  # Вызов метода через название класса
# mc = MyClass(1)
# mc.my_method(70)
# MyClass.on_sum_1(70)# Вызов метода класса через экземпляр


try:
    res = 100/0
except ZeroDivisionError:
    print("Деление на ноль!!!")
else:
    print(res)
finally:
    print("The end")



