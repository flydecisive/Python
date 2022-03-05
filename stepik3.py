num = int(input())
a = num // 100
b = num // 10 % 10
c = num % 10

print(num)
print(f'{a}{c}{b}')
print(f'{b}{a}{c}')
print(f'{b}{c}{a}')
print(f'{c}{a}{b}')
print(f'{c}{b}{a}')