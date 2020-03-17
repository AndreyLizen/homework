# 6) Продолжить работу над предыдущим заданием. Реализуйте механизм валидации вводимых пользователем
# данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать
# строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


in_storage = []
out_storage = []


class Warehouse:
    def __init__(self, name, quantity, measure, type_of_eq):
        self.type_of_eq = type_of_eq
        self.name = name
        self.quantity = quantity
        self.measure = measure
        self.position = {"Тип оборудования": self.type_of_eq, "Название": self.name, "Количество": self.quantity,
                         "Ед. измерения": self.measure}

    @staticmethod
    def validation_of_data(val):
        for k, v in val.items():
            if k == "Количество" and not v.isdigit():
                return "\033[1m\033[31m{}\033[0m".format("Количество задаётся только числом! Исправьте вводные данные!")
            else:
                return "Данные в порядке!"

    def acceptance(self, number):
        if self.validation_of_data(self.position) == "Данные в порядке!":
            in_storage.append([number, self.position])
            return "Принято на хранение: {}.\nОбщий перечень объектов на хранении:\n{}".format(self.position, '\n'.join(
                map(str, in_storage)))
        else:
            return self.validation_of_data(self.position)

    def out_of_stock(self):
        for i in range(len(in_storage)):
            if self.position in in_storage[i]:
                out_storage.append(in_storage[i])
                in_storage.remove(in_storage[i])
                break
        return "Выбыло со склада: {}.\nОбщий перечень выданных объектов:\n{}".format(self.position,
                                                                                     '\n'.join(map(str, out_storage)))


class OfficeEquipment(Warehouse):
    def __init__(self, name, quantity, measure, type_of_eq, price):
        super().__init__(name, quantity, measure, type_of_eq)
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, name, quantity, measure, price, is_color, type_of_eq="Принтер"):
        super().__init__(name, quantity, measure, type_of_eq, price)
        self.is_color = is_color


class Scanner(OfficeEquipment):
    def __init__(self, name, quantity, measure, price, type_of_scanning, type_of_eq="Сканер"):
        super().__init__(name, quantity, measure, type_of_eq, price)
        self.type_of_scanning = type_of_scanning


class Xerox(OfficeEquipment):
    def __init__(self, name, quantity, measure, price, is_big, type_of_eq="Ксерокс"):
        super().__init__(name, quantity, measure, type_of_eq, price)
        self.is_big = is_big


p = Printer("Canon", 5, "шт.", 5000, True)
s = Scanner("HP", 10, "шт.", 10000, "DRK-120")
x = Xerox("Xerox", 15, "шт.", 50000, True)
p.acceptance(1)
s.acceptance(2)
print(x.acceptance(3))
print(s.out_of_stock())
print("Общий перечень объектов на хранении:\n{}".format('\n'.join(map(str, in_storage))))
