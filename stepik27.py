side_1 = int(input())
side_2 = int(input())
side_3 = int(input())

sq_2_3 = side_2 ** 2 + side_3 ** 2
sq_1_3 = side_1 ** 2 + side_3 ** 2
sq_1_2 = side_1 ** 2 + side_2 ** 2

    
if side_1 == side_2 == side_3:
    print('Равносторонний')
elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
    print('Равнобедренный')
elif side_1 != side_2 and side_2 != side_3:
    print('Разносторонний')
