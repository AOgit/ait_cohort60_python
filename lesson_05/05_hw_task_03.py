# Task 3.*** (задание повышенной сложности, необязательное, только для желающих).
# Напишите программу, которая запрашивает у пользователя его имя, возраст и город проживания,
# а затем формирует приветственное сообщение с использованием функций и конкатенации строк.
#
# Создайте функцию get_user_info(), которая будет запрашивать у пользователя его имя,
# возраст и город и сохранять эти данные в переменных.
#
# Вызывать функцию generate_greeting(name, age, city),
# которая в свою очередь будет выводить на экран приветственное сообщение, используя конкатенацию строк.


def get_user_info():
    name = input("Имя: ")
    age = input("Возраст: ")
    city = input("Город: ")
    generate_greeting(name, age, city)

def generate_greeting(name, age, city):
    print(f"Привет, меня зовут {name}. Мне {age} лет и я живу в г. {city}.")

get_user_info()


