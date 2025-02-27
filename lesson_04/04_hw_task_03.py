# Task 3. *** (задание повышенной сложности, необязательное, только для желающих).
# Вы в ресторане с друзьями и нужно разделить счёт.
# Напишите программу, которая считает сколько чаевых оставить,
# сколько будет итоговая сумма счёта и как разделить эту сумму между несколькими людьми.
#
# Запросите у пользователя:
# Сумму счёта (переменная total_bill),
# Процент чаевых, который нужно оставить (переменная tip_percentage),
# Количество людей, на которых нужно разделить счёт (переменная people).
#
# Вывести на экран следующие результаты:
# Общую сумму к оплате без чаевых.
# Общую сумму чаевых.
# Общую сумму к оплате с чаевыми.
# Сумму, которую должен заплатить каждый человек.


total_bill = float(input("Сумма счёта: "))
tip_percentage = int(input("Процент чаевых: "))
people = int(input("Количество людей: "))

tips_amount = total_bill * (tip_percentage/100)
total_amount_with_tips = total_bill + tips_amount
amount_per_person = total_amount_with_tips / people

print("Сумма чека:", total_bill, "у.е.")
print(f"Чаевые: {tips_amount:.2f} у.е.")
print(f"Сумма с чаевыми: {total_amount_with_tips:.2f} у.е.")
print(f"Сумма на человека: {amount_per_person:.2f} у.е.")