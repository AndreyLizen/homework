# 5)Продолжить работу над предыдущим заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц
# оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

in_storage = []
out_storage = []


class Warehouse:
    def __init__(self, type_of_eq, name, quantity, measure):
        self.type_of_eq = type_of_eq
        self.name = name
        self.quantity = quantity
        self.measure = measure
        self.position = {"Тип оборудования": self.type_of_eq, "Название": self.name, "Количество": self.quantity,
                         "Ед. измерения": self.measure}

    def acceptance(self, number):
        in_storage.append([number, self.position])

        return "Принято на хранение: {}.\nОбщий перечень объектов на хранении:\n{}".format(self.position, '\n'.join(map(str, in_storage)))

    def out_of_stock(self):
        for i in range(len(in_storage)):
            if self.position in in_storage[i]:
                out_storage.append(in_storage[i])
                in_storage.remove(in_storage[i])
                break
        return "Выбыло со склада: {}.\nОбщий перечень выданных объектов:\n{}".format(self.position, '\n'.join(map(str, out_storage)))


class OfficeEquipment:
    def __init__(self, name, price, quantity, measure, type_of_eq):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.measure = measure
        self.type_of_eq = type_of_eq


class Printer(OfficeEquipment):
    def __init__(self, name, price, quantity, measure, is_color):
        super().__init__(name, price, quantity, measure, type_of_eq='Принтер')
        self.is_color = is_color


class Scanner(OfficeEquipment):
    def __init__(self, name, price, quantity, measure, type_of_scanning):
        super().__init__(name, price, quantity, measure, type_of_eq='Сканер')
        self.type_of_scanning = type_of_scanning


class Xerox(OfficeEquipment):
    def __init__(self, name, price, quantity, measure, is_big):
        super().__init__(name, price, quantity, measure, type_of_eq='Ксерокс')
        self.is_big = is_big


w = Warehouse("Принтер", "Canon", 5, "шт.")
w1 = Warehouse("Сканер", "HP", 10, "шт.")
w2 = Warehouse("Ксерокс", "Xerox", 15, "шт.")
w.acceptance(1)
w1.acceptance(2)
print(w2.acceptance(3))
print(w1.out_of_stock())
print("Общий перечень объектов на хранении:\n{}".format('\n'.join(map(str, in_storage))))
