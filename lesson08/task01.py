# 1) Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
# @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def turn_to_digit(cls, date):
        stop = False
        for i in range(len(date.split('-'))):
            if not date.split('-')[i].isdigit():
                stop = True
                break
        if len(date.split('-')) != 3 or stop:
            return "Error"
        else:
            Date.date = list(map(int, date.split('-')))
            return Date.date

    @staticmethod
    def validation_of_date(val):
        if val[1] < 1 or val[1] > 12:
            return "\033[1m\033[31m{}\033[0m".format("Задан неправильный месяц! Исправьте вводные данные!")
        elif val[0] < 1 or val[0] > 31:
            return "\033[1m\033[31m{}\033[0m".format("Задано неправильное число! Исправьте вводные данные!")
        elif val[0] == 30 and val[1] == 2:  # Високосные года проверять надо, но здесь не будем
            return "\033[1m\033[31m{}\033[0m".format("30-го февраля не бывает! Исправьте вводные данные!")
        elif val[0] == 31 and val[1] == 2 or val[1] == 4 or val[1] == 6 or val[1] == 9 or val[1] == 11:
            return "\033[1m\033[31m{}\033[0m".format("Задано неправильное число месяца! Исправьте вводные данные!")
        else:
            return f'Число: {val[0]}\nМесяц: {val[1]}\nГод: {val[2]}'

    def __str__(self):
        if Date.turn_to_digit(self.date) != "Error":
            return self.validation_of_date(Date.turn_to_digit(self.date))
        else:
            return "\033[1m\033[31m{}\033[0m".format("Дата задается числами в формате «день-месяц-год»! Проверьте и исправьте вводные данные!")


d = Date("31-09-88")
d1 = Date("30-33-88")
d2 = Date("33-03-88")
d3 = Date("13-03-2019")
d4 = Date("ddmmyyyy")
print(d)
print(d1)
print(d2)
print(d3)
print(d4)