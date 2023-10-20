salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
total_money = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for month in range(months):
    total_money = total_money + spend * (1 + increase) ** month - salary
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(total_money, 2))
