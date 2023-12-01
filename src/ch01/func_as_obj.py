def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def apply_operation(func, value):
    """Apply the given function to the value."""
    return func(value)

# Using functions as objects
result_square = apply_operation(square, 5)
result_cube = apply_operation(cube, 4)

# Print the results
print(f"Square of 5: {result_square}")
print(f"Cube of 4: {result_cube}")
