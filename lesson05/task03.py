# 3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии
# этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open("task03_file.txt", "r", encoding='utf-8') as f:
    my_list = f.read().split()
print(my_list)

small_salary = {my_list[i - 1]: my_list[i] for i in range(1, len(my_list), 2) if float(my_list[i]) < 20000.00}
print("Следующие сотрудники имеют зарплату менее 20000.00")
for k, v in small_salary.items():
    print(f'{k:<10}{v}')

salaries = 0
employees = 0
for i in range(1, len(my_list), 2):
    salaries = salaries + float(my_list[i])
    employees = employees + 1
print(f"Средняя зарплата среди {employees} сотрудников: {(salaries / employees):.2f}")