from math import sqrt

a = float(input())
b = float(input())
c = float(input())

diskriminant = b ** 2 - 4 * a * c

if diskriminant < 0:
    print('Нет корней')
elif diskriminant == 0:
    print(-b / (2 * a))
else:
    root_1 = (-b + sqrt(diskriminant)) / (2 * a)
    root_2 = (-b - sqrt(diskriminant)) / (2 * a)
    if root_1 > root_2:
        print(f'{root_2}\n{root_1}')
    else:
        print(f'{root_1}\n{root_2}')