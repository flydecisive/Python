dog_age = float(input())
first_2_years = 10.5
after_2_years = 4

if dog_age <= 2:
    result = dog_age * first_2_years
else:
    result = 2 * first_2_years + (dog_age - 2) * after_2_years

print(result)