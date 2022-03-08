less_1_liter = int(input('Введите количество бутылок менее 1 литра: '))
more_1_liter = int(input('Введите количество бутылок более 1 литра: '))

less_1_liter_coast = 0.1
more_1_liter_coast = 0.25

money_less = less_1_liter * less_1_liter_coast
money_more = more_1_liter * more_1_liter_coast

total_coast = money_less + money_more
total_coast = round(total_coast, 3)

print(f'Полная стоимость бутылок = {total_coast}$')