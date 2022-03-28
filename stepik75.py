from math import log

finish = int(input())

sum = 1

for i in range(2, finish + 1):
    sum += 1 / i

sum -= log(finish)
print(sum)