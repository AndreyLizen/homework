# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def user_data(name, surname, year_of_birth, current_city, email, phone):
    print(f'Данные пользователя: {name} {surname}, {year_of_birth}г.р., город {current_city}, тел.{phone}, email {email}')
def input_data():
    name = input("Введите ваше имя: ")
    surname = input("Введите вашу фамилию: ")
    year_of_birth = input("Введите ваш год рождения: ")
    current_city = input("Введите ваш город проживания: ")
    email = input("Введите ваш email: ")
    phone = input("Введите ваш номер телефона")
    user_data(current_city=current_city, name=name, year_of_birth=year_of_birth, email=email, surname=surname, phone=phone)
input_data()


