def multiplier(*args):
    total = 1
    for number in args:
        total *= number
    return total
    
resultado1 = multiplier(2,10)
print (resultado1)
