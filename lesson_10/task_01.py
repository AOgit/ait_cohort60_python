# Списки
empty_list = []
numbers = [5, 2, 3, 4, 7]

list1 = numbers[0]

print(list1)

fruits = ["Apple", "Banana", "Kiwi", "Cherry"]
for fruit in fruits:
    print(fruit)

for i in range(0,5):
    print(i)

print("==========================")
numbers = [5, 10, 15, 20]

for number in numbers:
    print(number)
print("==========================")
# Max element of list
print(numbers[len(numbers) - 1])

for i in range(len(numbers)):
    print(f"Индекс: {i} значение: {numbers[i]}")

print("==========================")
for i in range(1, 11):
    print(i)
print("==========================")

for i in range(5, -10, -2):
    print(i)
print("==========================")

for num in range(1,6):
    if num == 3:
        print("Нашел 3. Останавливаем цикл")
        break
    print(num)

