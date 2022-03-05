num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
num_4 = int(input())

min = num_1
if num_2 < min:
    min = num_2
if num_3 < min:
    min = num_3
if num_4 < min:
    min = num_4

print(min)