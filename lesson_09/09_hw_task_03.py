# Task 3. *** (задание повышенной сложности, необязательное, только для желающих).
# Напишите программу, которая запрашивает у пользователя целое число N,
# вычисляет первые N чисел последовательности Фибоначчи и выводит их на экран.
#
# Числа Фибоначчи — это последовательность, где каждое число является суммой двух предыдущих,
# начиная с чисел 0 и 1.

number = int(input("Введите целое число N\nдля вычисления первых N чисел\nпоследовательности Фибоначчи: "))
if number < 0:
    print("Введите число больше нуля")
    exit()

print("Отображаем через цикл")
counter = 1
Fn1 = Fn2 = 0
while counter <= number:
    if counter == 2:
        Fn2 = 1
    Fn = Fn1 + Fn2
    print(Fn, end=", ")
    Fn2 = Fn1
    Fn1 = Fn
    counter += 1

print("\nОтображаем через рекурсию")
counter = 1
Fn1 = Fn2 = 0
def fibonacci(counter, number, Fn1, Fn2):
    if counter <= number:
        if counter == 2:
            Fn2 = 1
        Fn = Fn1 + Fn2
        print(Fn, end=", ")
        Fn2 = Fn1
        Fn1 = Fn
        counter += 1
        return fibonacci(counter, number, Fn1, Fn2)

fibonacci(counter, number, Fn1, Fn2)



