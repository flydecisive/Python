year = int(input())

last_num = year % 10
prelast_num = year / 10 % 10

if last_num == 0 and prelast_num == 0:
    print('YES')
else:
    print('NO')