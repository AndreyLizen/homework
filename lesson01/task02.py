# 2)Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
number = int(input("Введите, пожалуйста, число секунд для перевода в формат 'чч:мм:сс': "))
hours = number // 3600
minutes = (number % 3600) // 60
seconds = number % 60
print(f"Время в формате 'чч:мм:сс' {hours:2d}:{minutes:2d}:{seconds:2d}")
if int(hours) > 99:
    print("Внимание! Количество часов >99, это превышает допустимый формат вывода!")