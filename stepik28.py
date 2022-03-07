num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

mid = num_1

if (num_2 <= num_1 and num_2 >= num_3) or (num_2 >= num_1 and num_2 <= num_3):
    mid = num_2
elif (num_3 <= num_1 and num_3 >= num_2) or (num_3 >= num_1 and num_3 <= num_2):
    mid = num_3

print(mid)