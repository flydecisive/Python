num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


if num_2 >= num_1 and num_2 >= num_3:
    if num_1 >= num_3:
        print(f'{num_2}\n{num_1}\n{num_3}')
    else:
        print(f'{num_2}\n{num_3}\n{num_1}')
elif num_3 >= num_1 and num_3 >= num_2:
    if num_1 >= num_2:
        print(f'{num_3}\n{num_1}\n{num_2}')
    else:
        print(f'{num_3}\n{num_2}\n{num_1}')
else:
    if num_2 >= num_3:
        print(f'{num_1}\n{num_2}\n{num_3}')
    else:
        print(f'{num_1}\n{num_3}\n{num_2}')
