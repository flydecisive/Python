side_1 = int(input())
side_2 = int(input())
side_3 = int(input())

sum_2_3 = side_2 + side_3
sum_1_3 = side_1 + side_3
sum_1_2 = side_1 + side_2

if side_1 < sum_2_3 and side_2 < sum_1_3 and side_3 < sum_1_2:
    result = 'YES'
else:
    result = 'NO'

print(result)