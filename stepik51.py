city_1 = input()
city_2 = input()
city_3 = input()

city_1_len = len(city_1)
city_2_len = len(city_2)
city_3_len = len(city_3)

max_city_len = max(city_1_len, city_2_len, city_3_len)
min_city_len = min(city_1_len, city_2_len, city_3_len)

if min_city_len == city_1_len:
    print(city_1)
elif min_city_len == city_2_len:
    print(city_2)
else:
    print(city_3)

if max_city_len == city_1_len:
    print(city_1)
elif max_city_len == city_2_len:
    print(city_2)
else:
    print(city_3)