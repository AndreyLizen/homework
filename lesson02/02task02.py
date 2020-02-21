# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
my_list = []
lenght_of_list = 5
i = 1
while i <= lenght_of_list:
    my_list.append(input(f'Введите {i}й элемент списка из {lenght_of_list}: '))
    i += 1
print(f'Полученный список: {my_list}')
new_list = []
i = 1
while i <= lenght_of_list:
    if i == lenght_of_list:
        new_list.append(my_list[i - 1])
        break
    new_list.append(my_list[i])
    new_list.append(my_list[i - 1])
    i = i + 2
print(f'Измененный список: {new_list}')
