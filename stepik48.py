from math import pi, tan

n = int(input())
a = float(input())

area = (n * a ** 2) / (4 * tan(pi/ n))
print(area)