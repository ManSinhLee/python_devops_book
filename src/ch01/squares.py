squares = []
for i in range(10):
    squared = i * i
    squares.append(squared)

print(squares)

squares = [i*i for i in range(10)]
print(squares)

squares = [i*i for i in range(10) if i%2==0]
print(squares)
