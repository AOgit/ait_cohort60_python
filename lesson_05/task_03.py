# Task 3. Самостоятельная работа.
# Исходные данные: есть склад размером 28 на 12, длина стола – 4, ширина стола - 2.
# Напишите программу, которая сохраняет эти данные в переменных, вычисляет и выводит в консоль,
# сколько столов поместится на склад.
# В программе должна быть отдельная функция, которая вычисляет площадь (независимо от того,
# площадь чего вычисляется, стола или склада).

ware_width = 28
ware_length = 12
table_width = 2
table_length = 4

def square(width, length):
    return  width * length



print(f"На склад поместится {square(ware_width, ware_length) / 
                             square(table_width, table_length):.0f} столa(ов)")