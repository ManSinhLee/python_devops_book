def add(a, b):
    return a + b 

def sub(a, b):
    return a - b 

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero."

a = 6
b = 9

print(f"Addition: {a} + {b} = {add(a, b)}")
print(f"Subtraction: {a} - {b} = {sub(a, b)}")
print(f"Multiplication: {a} * {b} = {mul(a, b)}")
print(f"Division: {a} + {b} = {div(a, b)}")