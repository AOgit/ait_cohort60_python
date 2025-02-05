# Task 3. *** (задание повышенной сложности, необязательное, только для желающих).
# Напишите функцию, которая принимает четыре числа в качестве параметров.
# Функция должна возвращать True в том случае, если первое число делится без остатка на второе,
# а третье при этом на четвёртое.
#
# Также функция должна возвращать True, если первое условие не выполняется,
# но при этом второе и четвёртое числа являются нечётными.
# Во всех остальных случаях функция должна возвращать False.
#
# Передайте в функцию три разных набора чисел и выведите результаты на экран.

def is_numbers_passed(num1: int, num2: int, num3: int, num4: int) -> bool:
    first_condition: bool = not is_rem(num1, num2) and not is_rem(num3, num4)
    second_condition: bool = not first_condition and is_odd(num2) and is_odd(num4)
    return first_condition or second_condition

def is_rem(number1: int, number2: int) -> bool:
    return number1 % number2 != 0

def is_odd(number: int) -> bool:
    return number % 2 !=0

print(is_numbers_passed(10, 2, 9, 3))
print(is_numbers_passed(8, 3, 6, 5))
print(is_numbers_passed(7, 3, 6, 4))
print(is_numbers_passed(12, 4, 8, 2))


