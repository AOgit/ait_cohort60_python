# Task1
# Напишите программу, которая считает произведение двух чисел.
# Программа должна запрашивать оба этих числа у пользователя. Рассчитайте произведение и выведите в консоль:
# второго и второго числа,
# второго и первого числа,
# первого и первого числа.

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

multi_22 = number2 * number2
multi_21 = number2 * number1
multi_11 = number1 * number1

print(multi_22)
print(multi_21)
print(multi_11)
