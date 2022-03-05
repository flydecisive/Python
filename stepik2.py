num = int(input())
digit_1 = num // 100
digit_2 = num // 10 % 10
digit_3 = num % 10

sum_digits = digit_1 + digit_2 + digit_3
mult_digits = digit_1 * digit_2 * digit_3

print(f'Сумма цифр = {sum_digits}')
print(f'Произведение цифр = {mult_digits}')