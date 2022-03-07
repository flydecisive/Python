num = int(input())

digit_1 = num // 100
digit_2 = num // 10 % 10
digit_3 = num % 10

max_n = max(digit_1, digit_2, digit_3)
min_n = min(digit_1, digit_2, digit_3)

if digit_1 > min_n and digit_1 < max_n:
    mid_n = digit_1
elif digit_2 > min_n and digit_2 < max_n:
    mid_n = digit_2
else:
    mid_n = digit_3

dif_max_min = max_n - min_n


if dif_max_min == mid_n:
    print('Число интересное')
else:
    print('Число неинтересное')