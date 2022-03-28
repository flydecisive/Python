from math import pow

start = int(input())
finish = int(input())

count = 0

for i in range(start, finish + 1):
    cube = pow(i, 3)
    digit = cube % 10
    if digit == 4 or digit == 9:
        count += 1

print(count)
    