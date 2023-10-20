salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

delta = 0
money_capital = 0
first_month = 1

for i in range(first_month, months + 1):
    if i == 1:
        delta = spend - salary
    else:
        spend *= (1 + increase)
        delta = spend - salary

    money_capital += delta

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital, 2))
