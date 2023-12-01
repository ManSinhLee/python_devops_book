# Example: Check if a number is positive, negative, or zero and if it's even or odd

# Get a number from the user
user_input = int(input("Enter an integer: "))

# Check if the number is positive, negative, or zero
if user_input > 0:
    print("The number is positive.")
    # Nested if/else to check if the positive number is even or odd
    if user_input % 2 == 0:
        print("And it's an even number.")
    else:
        print("And it's an odd number.")
elif user_input < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
