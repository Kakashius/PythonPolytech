salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
month = 1
money_capital = spend - salary  # 1-ый месяц
while months > month:
    spend += spend * increase
    money_capital += spend - salary
    month += 1

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
