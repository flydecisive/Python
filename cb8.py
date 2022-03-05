def filter_string(text, symbol):
    symbol = symbol.lower()
    new_text = ''
    for char in text:
        if symbol != char.lower():
            new_text += char
    return new_text

print(filter_string('If I look forward I am win', 'i'))

