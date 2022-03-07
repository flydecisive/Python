num = int(input())

if (num // 1000 >= 1 and num // 1000 <= 9) and (num % 17 == 0 or num % 7 == 0):
    result = 'YES'
else:
    result = 'NO'