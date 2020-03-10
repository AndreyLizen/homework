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


    # def __add__(self, other):
    #     return MyClass1(self.param1 + other.param1, self.param2 + other.param2)

    def __str__(self):
        for row in range(len(self.matrix)):
            print((self.matrix[row][x] for x in range(len(self.matrix[row]))), end='')


m1 = Matrix([[1,2],[3,4]])

print().__str__()

m2 = [1, 2]
for i in m2:
    print(str(i) + " ", end='')