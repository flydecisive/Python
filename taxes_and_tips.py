order_price = float(input())
taxes = 0.13
tips = 0.18

taxes_coast = order_price * taxes
tips_coast = order_price * tips

total_coast = order_price + taxes_coast + tips_coast

print(f'Налоги - {taxes_coast}')
print(f'Чаевые - {tips_coast}')
print(f'Общая сумма - {total_coast}')