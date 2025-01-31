'''
Исходные данные:
курс евро к доллару - 1.09.
У Вас на руках 1000 долларов.
Ставка по банковскому вкладу в евро - 5% годовых.
Напишите программу, которая считает сумму Вашего чистого дохода в евро и в долларах,
если Вы положите деньги на вклад на три года, учитывая, что проценты на вклад начисляются ежегодно.
'''

euro_usd_rate = 1.09
deposit_body_usd = 1000
bank_rate_euro = 5
years = 3

# Рассчитываем сумму в евро
deposit_body_euro = deposit_body_usd / euro_usd_rate
# print(deposit_body_euro)

# Рассчитываем общую конечную сумму в евро
total_final_amount_euro = deposit_body_euro * ((1 + bank_rate_euro / 100)**years)
# print(total_final_amount_euro)

# Рассчитываем чистые суммы в евро и долларах
net_income_euro = total_final_amount_euro - deposit_body_euro
net_income_usd = net_income_euro * euro_usd_rate

print(f"Ваш чистый доход: {net_income_euro:.2f} евро или {net_income_usd:.2f} долларов")
