# 4) Создать (не программно) текстовый файл со следующим содержимым:
# One - 1 Two - 2 Three - 3 Four - 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

print("Данная программа считывает построчно один файл и записывает построчно данные в другой файл.")
dict_for_translate = {"Один": 1, "Два": 2, "Три": 3, "Четыре": 4, "Пять": 5, "Шесть": 6, "Семь": 7}
f = open("task04_file1.txt", "r")
g = open("task04_file2.txt", "w", encoding='utf-8')
while True:
    new_str = f.readline()
    if not new_str:
        break
    new_str_list = new_str.replace('\n', '').split(' - ')
    print(new_str_list)
    for key, val in dict_for_translate.items():
        if int(new_str_list[1]) == val:
            g.write(f'{key:<8} - {val}\n')
            print(f'{key} - {val}')
f.close()
g.close()