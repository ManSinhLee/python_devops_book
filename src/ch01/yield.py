def count():
    n = 0
    while True:
        n += 1
        yield n

counter = count()
print("Counter: ", end=" ")
for i in range(10):
    print(next(counter), end=" ")    

def fib():
    first = 0
    last = 1
    while True:
        first, last = last, first + last
        yield first

f = fib()
print("\nFibonnaci: ", end=" ")
for i in range(10):
    print(next(f), end=" ")