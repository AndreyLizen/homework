# 3)Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# # Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
number = int(input("Введите, пожалуйста, целое положительное число n: "))
number1 = int(f"{number}{number}")
number2 = int(f"{number}{number}{number}")
summa = number + number1 + number2
print(f"Сумма чисел n + nn + nnn составляет: {summa}.")