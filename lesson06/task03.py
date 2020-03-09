# 3)Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
# position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс
# Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного
# имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, wage, bonus, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, wage, bonus, position=None):
        super().__init__(name, surname, wage, bonus, position)

    def get_full_name(self):
        return f"Полное имя сотрудника: {self.name} {self.surname}. "

    def get_total_income(self):
        return f"Полный доход сотрудника: {sum(self._income.values())}$"


a = Position("Джон", "Блэк", 2000, 1000)
print(a.get_full_name(), a.get_total_income())

b = Position("Марк", "Твен", 0, 10000)
print(b.get_full_name(), b.get_total_income())
