money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

month = 0

while money_capital > spend:
    money_capital += salary
    money_capital -= spend * (1 + increase) ** month  # данная запись учитывает отсутствие роста цен в первый месяц
    month+= 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
