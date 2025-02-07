# Task 2.
# Напишите программу, которая выводит на экран все чётные числа в порядке убывания из диапазона от 100 до 80.

counter = 100
while counter >= 80:
    if counter % 2 == 0:
        print(counter)
    counter -= 1
