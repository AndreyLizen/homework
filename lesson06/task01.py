# 1)Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.  Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав
# описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
# соответствующее сообщение и завершать скрипт.


import time

class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        print(f"Цвет светофора: {self.__color}")
        while True:
            print("\033[31m {}\033[0m".format("Красный"))
            time.sleep(7)
            print("\033[33m {}\033[0m".format("Жёлтый"))
            time.sleep(2)
            print("\033[32m {}\033[0m".format("Зелёный"))
            time.sleep(11)


r = TrafficLight("red")
r.running()

