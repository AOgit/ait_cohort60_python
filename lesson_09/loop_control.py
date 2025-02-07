# break
# continue


# вариант реализации без break
sum = 0
number = int(input("Введите число (0 для выхода): "))
while number:
    sum += number
    number = int(input("Введите число (0 для выхода): "))

print(sum)