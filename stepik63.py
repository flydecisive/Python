start = int(input())
stop = int(input())

for i in range(start, stop - 1, -1):
    if i % 2 != 0:
        print(i)