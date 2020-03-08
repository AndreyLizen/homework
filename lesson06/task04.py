# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).  А также методы: go, stop, turn(direction), которые должны
# сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
# показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
# скорости.Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите  результат. Выполните вызов методов и также покажите результат.

from random import randint


class Car:
    def __init__(self, speed, color, name, is_police):
        self.color = color
        self.name = name
        self.speed = speed
        self.is_police = is_police

    def go(self):
        if self.is_police:
            return f"Полицейская машина {self.name}, цвет {self.color}, начала движение."
        else:
            return f"Машина {self.name}, цвет {self.color}, начала движение."

    def show_speed(self):
        return f"Машина едет со скоростью {self.speed}км/ч."

    def stop(self):
        return f"Машина {self.name} остановилась."

    def turn_direction(self):
        i = randint(1, 3)
        if i == 1:
            return f"Машина повернула налево."
        elif i == 2:
            return f"Машина поехала прямо."
        else:
            return f"Машина повернула направо."


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f"Машина едет со скоростью {self.speed}км/ч." + "\033[1m\033[31m {}\033[0m".format(
                "Внимание! Вы превысили скорость!")
        else:
            return f"Машина едет со скоростью {self.speed}км/ч."


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f"Машина едет со скоростью {self.speed}км/ч." + "\033[1m\033[31m {}\033[0m".format(
                "Внимание! Вы превысили скорость!")
        else:
            return f"Машина едет со скоростью {self.speed}км/ч."


s = SportCar(120, "красный", "'Астон Мартин'")
print(s.go(), s.turn_direction(), '\n' + s.show_speed(), s.stop(), '\n')
p = PoliceCar(100, "белый", "'Шевроле Круз'")
print(p.go(), p.turn_direction(), '\n' + p.show_speed(), p.stop(), '\n')
t = TownCar(70, "чёрный", "'Дацун Мидо'")
print(t.go(), t.turn_direction(), '\n' + t.show_speed(), t.stop(), '\n')
w = WorkCar(50, "оранжевый", "- цементовоз")
print(w.go(), w.turn_direction(), '\n' + w.show_speed(), w.stop(), '\n')
