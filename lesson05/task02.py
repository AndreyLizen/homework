# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
# количества строк, количества слов в каждой строке.

print("Данная программа читает файл и подсчитывает количество строк, количество слов в строке (разделитель - пробел), а также в файле в целом.")
f = open("task02_file.txt", "r", encoding='utf-8')
str_count = 0
while True:
    new_str = f.readline()
    if not new_str:
        break
    print(f"Количество слов в {str_count + 1}й строке {new_str.split()}: {len(new_str.split())}")
    str_count += 1
f.close()

with open("task02_file.txt", "r", encoding='utf-8') as f:
    print(f"Всего строк: {str_count}, всего слов: {len(f.read().split())}")

