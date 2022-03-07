number = int(input())

if number >= 0 and number <= 36:
    if number == 0:
        print('зеленый')
    elif number >= 1 and number <= 10:
        if number % 2 == 0:
            print('черный')
        else:
            print('красный')
    elif number >= 11 and number <= 18:
        if number % 2 == 0:
            print('красный')
        else:
            print('черный')
    elif number >= 19 and number <= 28:
        if number % 2 == 0:
            print('черный')
        else:
            print('красный')
    elif number >= 29 and number <= 36:
        if number % 2 == 0:
            print('красный')
        else:
            print('черный')
else:
    print('ошибка ввода')