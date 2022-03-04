def string_or_not(argument):
    result = isinstance(argument, str)
    return result and 'yes' or 'no'

print(string_or_not(3))