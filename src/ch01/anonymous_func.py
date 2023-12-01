# Regular function
def square(x):
    return x ** 2

# Equivalent lambda function
lambda_square = lambda x: x ** 2

# Using both functions
result_regular = square(5)
result_lambda = lambda_square(5)

print(f"Square using regular function: {result_regular}")
print(f"Square using lambda function: {result_lambda}")

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)


items = [[0, 'a', 2], [5, 'b', 0], [2, 'c', 1]]
print(f"Sorted: {sorted(items)}")

def second(item):
    '''return second entry'''
    return item[1]

print(f"Sorted: {sorted(items, key=second)}")