# 1)Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        try:
            result = []
            stop = False
            for row in range(len(self.matrix)):
                if len(self.matrix) != len(other.matrix) or stop:  # Проверка соответствия размерности матрицы
                    break
                result.append([])
                for x in range(len(self.matrix[row])):
                    if len(self.matrix[row]) != len(other.matrix[row]):  # Проверка соответствия размерности матрицы
                        stop = True
                        break
                    result[row].append(0)
                    result[row][x] = self.matrix[row][x] + other.matrix[row][x]
            if len(self.matrix) != len(other.matrix) or stop:
                print("\033[1m\033[31m{}\033[0m".format(
                    "Математически сложение матриц имеет смысл только для идентичных по размерности матриц! Исправьте вводные данные!"))
            else:
                return Matrix(result)
        except TypeError:
            print("\033[1m\033[31m{}\033[0m".format(
                "Складывать можно только числа! Проверьте и исправьте вводные данные!"))

    def __str__(self):
        return str(self.print_matrix()).replace("None", "")

    def print_matrix(self):
        for row in range(len(self.matrix)):
            for x in range(len(self.matrix[row])):
                print(f"{self.matrix[row][x]:<4}", end=' ')
            print()


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1], [0, -1, -2]])
print(m1)
print(m2)
print(m1 + m2)

