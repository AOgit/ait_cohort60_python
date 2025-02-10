# Напишите Функцию, которая принимает список чисел.
# Функция должна вычислить и вернуть среднее арифметическое чисел, входящих в список.
#
# Подсказка: среднее арифметическое чисел: Это сумма чисел, разделенная на их количество.
#
# P.S. Реализовать защиту от деления на 0
# print_even_numbers([1, 2, 3, 4, 5, 6])
# print("=============")
# print_even_numbers([10, 15, 20, 25, 30])
# print_even_numbers([])

def average_numbers(numbers):
    quant = len(numbers)
    sum = 0
    for number in numbers:
        sum += number
    print("Массив чисел пустой" if quant == 0 else sum / quant)

numbers1 = [1,2,3,4,5,6]
numbers2 = [10, 15, 20, 25, 30]
numbers3 = []

average_numbers(numbers1)
average_numbers(numbers2)
average_numbers(numbers3)


