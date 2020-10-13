""" 2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_data(user_name, surname, birth_year, city, email, phone):
    """Returns user data in one line.

    Named arguments: user_name - name, surname - surname,
    birth_year - year of birth, city - city of residence,
    email - email, phone - phone.
    """
    print(f"Name: {user_name}, surname: {surname},"
          f" year of birth: {birth_year}, "
          f"city of residence: {city}, email: {email}, "
          f"phone: {phone}")


user_name = input("Enter your name: ")
surname = input("Enter your surname: ")
birth_year = input("Enter your year of birth: ")
city = input("Enter your city of residence: ")
email = input("Enter your email: ")
phone = input("Enter your phone: ")

user_data(user_name, surname, birth_year, city, email, phone)