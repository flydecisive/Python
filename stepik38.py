num = input()

dot_pos = num.find('.')
new_num = f'0{num[dot_pos:]}'
print(new_num)