# 2) Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу
# на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def division():
    try:
        a = int(input("Данная функция выполняет деление двух чисел - делимого и делителя. Введите делимое: "))
        b = int(input("Введите делитель: "))
        if b == 0:
            raise OwnError("Делить на ноль нельзя! Перезапустите программу и попробуйте ещё раз!")
    except ValueError:
        print("Вы ввели не число! Перезапустите программу и попробуйте ещё раз!")
    except OwnError as error:
        print(error)
    else:
        print(f"Результат деления {a} / {b} = {(a / b):.2f}")
    finally:
        print("\033[1m\033[30m\033[47m {}\033[0m".format("Программа завершена!"))


division()
