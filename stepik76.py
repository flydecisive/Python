from http.client import SWITCHING_PROTOCOLS
from math import pow

finish = int(input())

sum = 0

for i in range(1, finish + 1):
    square = pow(i, 2)
    digit = square % 10
    if digit == 2 or digit == 5 or digit == 8:
        sum += i

print(sum)
