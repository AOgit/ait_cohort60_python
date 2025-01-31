salary_per_hour = 120
hours = 7
bonus = 180
tax_rate = 20 # Відсотки

# Обчислення

salary_brutto = salary_per_hour * hours + bonus
tax = salary_brutto * tax_rate / 100 # обчислюємо х процентів від суми
salary_netto = salary_brutto - tax

# Виведення результатів
print(f"Співробітник отримає {salary_netto:.2f} у.е після вирахування податків")