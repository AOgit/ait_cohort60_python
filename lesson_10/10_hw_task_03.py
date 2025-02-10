# Task 3. *** (задание повышенной сложности, необязательное, только для желающих).
# Напишите функцию, которая принимает на вход список чисел,
# находит в нём максимальное и минимальное значения, и меняет их местами.

numbers = [3, -44, -2, 23, 2, 67, -5, 0]
print(numbers)

def min_max_shuffle(numbers):
    min_num_inx = max_num_inx = 0
    for n in range(len(numbers)):
        if  numbers[min_num_inx] > numbers[n]:
            min_num_inx = n
        if  numbers[max_num_inx] < numbers[n]:
            max_num_inx = n
    min = numbers[min_num_inx]
    numbers[min_num_inx] = numbers[max_num_inx]
    numbers[max_num_inx] = min
    return numbers

print(min_max_shuffle(numbers))


