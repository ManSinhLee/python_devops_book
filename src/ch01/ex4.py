# Write a generator that alternates between returning Even and Odd.
def alternate_even_odd():
    count = 0
    while True:
        if count % 2 == 0:
            yield "Even"
        else:
            yield "Odd"
        count += 1

# Example usage:
generator = alternate_even_odd()

# Print the first 5 values
for _ in range(5):
    print(next(generator))
