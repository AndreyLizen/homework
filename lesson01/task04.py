# 4) Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
number = int(input("Введите, пожалуйста, целое положительное число: "))
max_digit = 9
result = 0
while number > 0:
    digit = number % 10
    number = number // 10
    if digit == max_digit:
        result = max_digit
        break
    elif digit > result:
        result = digit
print(f'Наибольшая цифра в данном числе: {result}.')