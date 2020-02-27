# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def max_args_sum(a1, a2, a3):
    arg123 = [a1, a2, a3]
    max_arg1 = max(arg123)
    for el in arg123:
        if el == max_arg1:
            arg123.remove(el)
            break
    max_arg2 = max(arg123)
    print(f'Сумма двух наибольших аргументов: {max_arg1} + {max_arg2} = {max_arg1 + max_arg2}')

max_args_sum(-5, 0, 55)