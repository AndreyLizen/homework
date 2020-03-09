# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title='Общий'):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки. Метод '{self.title}'.")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки. Метод 'Ручка'.")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки. Метод 'Карандаш'.")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки. Метод 'Маркер'.")


s = Stationery()
s.draw()
p = Pen()
p.draw()
q = Pencil()
q.draw()
h = Handle()
h.draw()
