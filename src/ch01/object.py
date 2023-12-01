def double(input):
    '''double input'''
    return input*2

print(f"double memory address: {double}")
print(f"Type of funtion: {type(double)}")

def triple(input):
    ''''Triple input'''
    return input * 3

functions = [double, triple]

print(f"double and triple of input:", end=' ')
for function in functions:
    print(function(3), end=' ')