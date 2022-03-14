str_1 = input()
str_2 = input()
str_3 = input()

str_1_len = len(str_1)
str_2_len = len(str_2)
str_3_len = len(str_3)

max_str = max(str_1_len, str_2_len, str_3_len)
min_str = min(str_1_len, str_2_len, str_3_len)

if str_1_len < max_str and str_1_len > min_str:
    mid_str = str_1_len
elif str_2_len < max_str and str_2_len > min_str:
    mid_str = str_2_len
else:
    mid_str = str_3_len

diff_1 = abs(max_str - mid_str)
diff_2 = abs(mid_str - min_str)

if diff_1 == diff_2:
    print('YES')
else:
    print('NO')