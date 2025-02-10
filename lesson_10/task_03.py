numbers = [1, 3, 5, 4, 6, 6, 7, 8, 9, 44, 66, -20, -4, 33, 44]

min = numbers[0]
for number in numbers:
    if number < min:
        min = number

print(min)