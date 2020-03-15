# 4) Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс
# «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


class Warehouse:
    def __init__(self, type_of_eq, name, quantity, measure):
        self.type_of_eq = type_of_eq
        self.name = name
        self.quantity = quantity
        self.measure = measure
        self.position = {"Тип оборудования": self.type_of_eq, "Название": self.name, "Количество": self.quantity,
                         "Ед. измерения": self.measure}


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
