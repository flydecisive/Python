start = int(input())
stop = int(input())

for i in range(start, stop + 1):
    if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
        print(i)