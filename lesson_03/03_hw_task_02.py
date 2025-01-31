# Task2
# Бананы стоят 11 у.е., яблоки - 8 у.е.
# Вам нужно купить два килограмма бананов и три килограмма яблок. Сохраните все эти данные в переменных.
# Напишите программу, которая выводит на экран фразу
# "Для покупки Х килограммов бананов и Y килограммов яблок мне нужно Z у.е."
# В местах, где Х, Y, Z - нужно воспользоваться переменными.

bananas_price = 11
apples_price = 8
bananas_amount = None
apples_amount = None

while bananas_amount == None:
    try:
        bananas_amount = int(input("Кол-во бананов: "))
    except:
        print(f"Введенное значение должно быть числом")

while apples_amount == None:
    try:
        apples_amount = int(input("Кол-во яблок: "))
    except:
        print(f"Введенное значение должно быть числом")

total = bananas_price * bananas_amount + apples_price * apples_amount
print(f"Для покупки {bananas_amount} килограммов бананов и {apples_amount} килограммов яблок мне нужно {total} у.е.")