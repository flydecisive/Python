point = int(input())

if (point > -30 and point <= -2) or (point > 7 and point <= 25):
    result = 'Принадлежит'
else:
    result = 'Не принадлежит'

print(result)