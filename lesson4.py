# from sys import argv
#
# script_name, p1, p2, p3 = argv
#
# print('Имя скрипта: ', script_name)
# print("Параметр1: ", p1)
# print("Параметр2: ", p2)
# print("Параметр3: ", p3)

# my_list = [1, 2, 3, 4, 5, 6]
# new_list = [el + 10 for el in my_list]
# new_list1 = [el for el in my_list if el % 2 == 0]
# print(my_list)
# print(new_list)
# print(new_list1)
#
# s1 = 'abc'
# s2 = 'd'
# s3 = 'efg'
# new_list2 = [i + j + k for i in s1 for j in s2 for k in s3]
# print(new_list2)
#
# new_list3 = {el: el ** 2 for el in range(10,20)}
# new_list4 = {el ** 3 for el in range(5,10)}
# my_tuple = (2,4,6)
# new_list5 = (el +10 for el in my_tuple)
# print(new_list3)
# print(new_list4)
# print(next(new_list5))

# import random
# print(random.randint(0,10))

import random

# from random import randint, randrange
#
# print(randint(0, 10))
# print(randrange(0, 10, 3)) - от нуля не включая верхнюю границу с шагом 3

# generator = (par * par for par in range(5))
# print(generator)
# for el in generator:
#     print(el)
#
# def generator1():
#     for i in (10,20,30):
#         yield i
# g = generator1()
# print(g)
# for i in g:
#     print(i)

def cube(n):
    c_list = []
    for i in n:
        c_list.append(i ** 3)
    return c_list
print(cube([1,2,3,4]))

def cube1(n):
    for i in n:
        yield i ** 3
m = cube1([1,2,3,4,5])
for i in m:
    print(i)

from functools import reduce
def my_f(el0, el1):
    return el0 +el1
print(reduce(my_f, [1,2,3,4,5]))

from itertools import count, cycle
