money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
money_total = 0
total_month = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while money_capital >= money_total:
    money_total = money_total + (spend * ((1 + increase) ** total_month) - salary)
    total_month += 1
if money_total > money_capital:
    total_month -= 1
print("Количество месяцев, которое можно протянуть без долгов:", total_month)
