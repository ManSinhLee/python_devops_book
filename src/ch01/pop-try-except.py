# Example: Handling exceptions when using the pop() function

# Sample list
my_list = [1, 2, 3, 4, 5]
print(my_list)

try:
    # Attempt to pop an element from the list
    index_to_pop = int(input("Enter the index to pop: "))
    
    # Try to pop the element at the specified index
    popped_value = my_list.pop(index_to_pop)
    
    # Print the popped value
    print(f"The popped value is: {popped_value}")
    print(f"The updated list is: {my_list}")

except IndexError:
    # Handle the IndexError if the specified index is out of range
    print("Error: Index out of range. Please enter a valid index.")

except ValueError:
    # Handle the ValueError if the user enters a non-integer
    print("Error: Please enter a valid integer index.")

except Exception as e:
    # Handle other types of exceptions
    print(f"An unexpected error occurred: {e}")

# The program continues to execute after the try-except block
print("Program continues...")
