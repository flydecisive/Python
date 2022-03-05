num = int(input())
digit_1 = num // 1000
digit_2 = num // 100 % 10
digit_3 = num // 10 % 10
digit_4 = num % 10

edge_sum = digit_1 + digit_4
center_diff = digit_2 - digit_3

if edge_sum == center_diff:
    print('ДА')
else:
    print('НЕТ')