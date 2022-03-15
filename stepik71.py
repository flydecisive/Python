cell_x_1 = int(input())
cell_y_1 = int(input())
cell_x_2 = int(input())
cell_y_2 = int(input())

sum_cell_1 = cell_x_1 + cell_y_1
sum_cell_2 = cell_x_2 + cell_y_2

dif_x = abs(cell_x_1 - cell_x_2)
dif_y = abs(cell_y_1 - cell_y_2)

if sum_cell_1 % 2 == 0 and sum_cell_2 % 2 != 0 and ((dif_x == 1 and dif_y == 2) or (dif_x == 2 and dif_y == 1)):
    print('YES')
elif sum_cell_1 % 2 != 0 and sum_cell_2 % 2 == 0 and ((dif_x == 1 and dif_y == 2) or (dif_x == 2 and dif_y == 1)):
    print('YES')
else:
    print('NO')