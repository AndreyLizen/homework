# 1) Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#     Об окончании ввода данных свидетельствует пустая строка.

print("Данная программа записывает построчно данные в файл. При вводе пустой строки - конец записи.")
with open("task01_file.txt", "w", encoding='utf-8') as f:
    while True:
        new_str = input("Введите новую строку для записи в файл: ")
        if new_str == '':
            break
        f.write(f'{new_str}\n')
