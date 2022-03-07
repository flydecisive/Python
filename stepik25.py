x_1 = int(input())
y_1 = int(input())
x_2 = int(input())
y_2 = int(input())

abs_x = abs(x_2 - x_1)
abs_y= abs(y_2 - y_1)

if (x_1 == x_2 and abs_y == 1) or (y_1 == y_2 and abs_x == 1) or (abs_x == abs_y and abs_x == 1):
    result = 'YES'
else:
    result = 'NO'

print(result)