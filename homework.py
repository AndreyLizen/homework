# 1) Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
# number = 5
# text = "Введённое число: "
# print(f'{text}{number}')
#
# name = input("Введите, пожалуйста, свое имя: ")
# age = int(input("Введите, пожалуйста, свой возраст числом: "))
# print(f'{"Уважаемый(ая) " + name}, через 5 лет ваш возраст будет {age + 5}.')

# 2)Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
number = int(input("Введите, пожалуйста, число секунд для перевода в формат 'чч:мм:сс': "))
hours = number // 3600
# if hours <= 9:
#     hours = str(f"0{hours}")
minutes = (number % 3600) // 60
# if minutes <= 9:
#     minutes = str(f"0{minutes}")
seconds = number % 60
# if seconds <= 9:
#     seconds = str(f"0{seconds}")
print(f"Время в формате 'чч:мм:сс' {hours:02d}:{minutes:02d}:{seconds:02d}")
# if int(hours) > 99:
#     print("Внимание! Количество часов >99, это превышает допустимый формат вывода!")

# 3)Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# # Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
# number = int(input("Введите, пожалуйста, целое положительное число n: "))
# number1 = int(f"{number}{number}")
# number2 = int(f"{number}{number}{number}")
# summa = number + number1 + number2
# print(f"Сумма чисел n + nn + nnn составляет: {summa}.")

# 4)Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
# number = int(input("Введите, пожалуйста, целое положительное число: "))
# max_digit = 9
# result = 0
# while number > 0:
#     digit = number % 10
#     number = number // 10
#     if digit == max_digit:
#         result = max_digit
#         break
#     elif digit > result:
#         result = digit
# print(f'Наибольшая цифра в данном числе: {result}.')

# 5) Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль ​— выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма
# отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность
# сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
# revenue = int(input("Введите выручку в у.д.е. за отчетный период: "))
# costs = int(input("Введите издержки в у.д.е. за отчетный период: "))
# if revenue > costs:
#     profit = revenue - costs
#     profitability = profit / revenue * 100
#     print(f"Ваша прибыль за отчетный период составила {profit}у.д.е.")
#     print(f"Рентабельность за отчетный период составила {profitability:.2f}%.")
#     number_of_employees = int(input("Введите количество сотрудников фирмы: "))
#     profit_for_1 = profit / number_of_employees
#     print("Ваша прибыль в расчете на одного сотрудника за отчетный период составила {:.2f}у.д.е.".format(profit_for_1))
# else:
#     loss = costs - revenue
#     print(f'Вы не получили прибыли в отчетном периоде. Ваш убыток составил {loss}у.д.е.')
#
# # 6) Спортсмен занимается ежедневными пробежками. В первый день его результат составил ​a километров.
# # Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить
# # номер дня, на который результат спортсмена составит не менее ​b километров.
# # Программа должна принимать значения параметров ​a ​и ​b ​и выводить одно натуральное число ​—​ номер дня.
# start = int(input("Введите стартовый показатель в километрах для бегуна: "))
# finish = int(input("Введите целевой показатель в километрах для бегуна: "))
# result = 1
# while finish >= start:
#     start = start * 1.1
#     result += 1
# print(f"Прибавляя по 10% в день, бегун достигнет целевого показателя на {result}й день.")
