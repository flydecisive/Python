from random import random

def get_random_number():
    return round(random() * 9 + 1)

print(get_random_number())