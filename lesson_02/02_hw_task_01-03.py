"""
https://www.onlinegdb.com/
lesson 02 Home work
"""

# Task 1
candy_price = 3
budget = 27
print("Вы в состоянии купить", budget // candy_price, "конфет")

# Task 2
candy_price = 3
ice_cream_price = 5
print("Вам потребуется", 7*candy_price + 3*ice_cream_price, "у.е.")

# Task 3
euro_usd = 1.09
cookies_usd_price = 3.25
waffles_usd_price = 4.40

budget_euro = 10
total_euro = (cookies_usd_price * 0.5 + waffles_usd_price * 1.5) / euro_usd

print("Ваша сдача:",  round(budget_euro - total_euro, 2), "€")

