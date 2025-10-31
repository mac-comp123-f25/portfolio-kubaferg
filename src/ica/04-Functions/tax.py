def add_tax(price, tax_rate):
    print('add_tax inputs:',price, tax_rate)
    tax_amt = price * tax_rate
    print('return value:', tax_amt)
    return price + tax_amt
print(add_tax(25.99, 0.0725))