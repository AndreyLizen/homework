# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

my_string = input("Введите несколько слов, разделённых пробелами: ")
for ind, word in enumerate(my_string.split(), 1):
    print(f"{ind}. {word[:10]}")