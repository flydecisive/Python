num = int(input())

digit_1 = num // 1000
digit_2 = num // 100 % 10
digit_3 = num // 10 % 10
digit_4 = num % 10

print(f'Цифра в позиции тысяч равна {digit_1}')
print(f'Цифра в позиции сотен равна {digit_2}')
print(f'Цифра в позиции десятков равна {digit_3}')
print(f'Цифра в позиции единиц равна {digit_4}')