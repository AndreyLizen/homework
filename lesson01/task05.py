# 5) Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль ​— выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма
# отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность
# сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
revenue = int(input("Введите выручку в у.д.е. за отчетный период: "))
costs = int(input("Введите издержки в у.д.е. за отчетный период: "))
if revenue > costs:
    profit = revenue - costs
    profitability = profit / revenue * 100
    print(f"Ваша прибыль за отчетный период составила {profit}у.д.е.")
    print("Рентабельность за отчетный период составила {:.2f}%.".format (profitability))
    number_of_employees = int(input("Введите количество сотрудников фирмы: "))
    profit_for_1 = profit / number_of_employees
    print("Ваша прибыль в расчете на одного сотрудника за отчетный период составила {:.2f}у.д.е.".format(profit_for_1))
else:
    loss = costs - revenue
    print(f'Вы не получили прибыли в отчетном периоде. Ваш убыток составил {loss}у.д.е.')