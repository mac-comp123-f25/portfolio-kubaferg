def has_QOCD(x):
    if 'Q' in x or 'O' in x or 'C' in x or'D' in x:
        result = True
    else:
        result = False
    return result
x = input()
print(has_QOCD(x))