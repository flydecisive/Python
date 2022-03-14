organism_val = float(input())
day_increase = float(input())
days = int(input())
increased = organism_val

for i in range(days):
    print(f'{i + 1} {increased}')
    increased += increased * (day_increase / 100)