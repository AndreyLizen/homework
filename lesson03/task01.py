# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(a, b):
    print(f"Результат деления {a} / {b} = {(a / b):.2f}")
divident = int(input("Данная функция выполняет деление двух чисел - делимого и делителя. Введите делимое: "))
divisor = int(input("Введите делитель: "))
try:
    division(divident, divisor)
except ZeroDivisionError:
        print("Будьте внимательны! Делить на ноль нельзя!!")

