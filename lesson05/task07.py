# 7) Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее ​не включать.​
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь
# (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"​firm_1":​​5000,​"​firm_2":​3​000,​​"firm_3":​​1000}​, {"​average_profit":​​2000}​]
# Подсказка: использовать менеджер контекста.
total_list = []
average_profit = {}
with open("task07_file.txt", "r", encoding='utf-8') as f:
    my_list = f.read().split()
print(my_list)

# Делаем словарь фирм
firms = {my_list[i]: (int(my_list[i + 2]) - int(my_list[i + 3])) for i in range(0, len(my_list), 4)}
print(firms)

# Делаем словарь средней прибыли
total_profit = []
for v in firms.values():
    if v > 0:
        total_profit.append(v)
average_profit["average_profit"] = round((sum(total_profit) / len(total_profit)), 2)
print(average_profit)

# Итоговый список
total_list.append(firms)
total_list.append(average_profit)
print(total_list)

# Создание объекта json и сохранение его в файл json
import json
with open('task07.json', 'w', encoding='utf-8') as f:
    json_list = json.dump(total_list, f)
