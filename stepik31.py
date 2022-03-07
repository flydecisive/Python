a_1 = int(input())
b_1 = int(input())
a_2 = int(input())
b_2 = int(input())

if a_1 > b_2 or b_1 < a_2:
    print('пустое множество')
elif a_1 < a_2:
    if b_1 < b_2:
        print(f'{a_2} {b_1}')
    elif b_1 > b_2:
        print(f'{a_2} {b_2}')
    else:

elif a_1 > a_2:

elif a_1 == a_2:

elif a_1 == b_2:

elif a_2 == b_1:
