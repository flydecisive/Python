from math import *

num_1 = float(input())
num_2 = float(input())

average = (num_1 + num_2) / 2
geometric_mean = sqrt(num_1 * num_2)
harmonic_mean = (2 * num_1 * num_2) / (num_1 + num_2)
root_mean = sqrt((num_1 ** 2 + num_2 ** 2) / 2)

print(average)
print(geometric_mean)
print(harmonic_mean)
print(root_mean)