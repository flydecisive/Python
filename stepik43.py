import math

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

p = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
print(p)