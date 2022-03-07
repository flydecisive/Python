color_1 = input()
color_2 = input()

if color_1 == 'красный':
    if color_2 == 'красный':
        print('красный')
    elif color_2 == 'синий':
        print('фиолетовый')
    elif color_2 == 'желтый':
        print('оранжевый')
    else:
        print('ошибка цвета')
elif color_1 == 'синий':
    if color_2 == 'синий':
        print('синий')
    elif color_2 == 'красный':
        print('фиолетовый')
    elif color_2 == 'желтый':
        print('зеленый')
    else:
        print('ошибка цвета')
elif color_1 == 'желтый':
    if color_2 == 'желтый':
        print('желтый')
    elif color_2 == 'синий':
        print('зеленый')
    elif color_2 == 'красный':
        print('оранжевый')
    else:
        print('ошибка цвета')
else:
        print('ошибка цвета')
