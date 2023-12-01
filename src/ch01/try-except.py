# Example: Handling a division by zero exception

# Get two numbers from the user
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    
    # Attempt to perform the division
    result = numerator / denominator

    # Print the result if the division is successful
    print(f"The result of {numerator}/{denominator} is: {result}")

except ZeroDivisionError:
    # Handle the division by zero exception
    print("Error: Division by zero is not allowed.")

except ValueError:
    # Handle the ValueError (e.g., if the user enters a non-integer)
    print("Error: Please enter valid integers.")

except Exception as e:
    # Handle other types of exceptions
    print(f"An unexpected error occurred: {e}")

# The program continues to execute after the try-except block
print("Program continues...")
