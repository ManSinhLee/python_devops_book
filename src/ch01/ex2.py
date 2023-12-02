# Write a Python function that takes a string as an argument and prints whether it is upper or lowercase.
def check_case(input_string):
    """Print whether the given string is in upper or lowercase."""
    if input_string.isupper():
        print(f"The string '{input_string}' is in UPPERCASE.")
    elif input_string.islower():
        print(f"The string '{input_string}' is in lowercase.")
    else:
        print(f"The string '{input_string}' has a mix of uppercase and lowercase characters.")

# Example usage:
string_to_check1 = "HELLO"
string_to_check2 = "world"
string_to_check3 = "MixED"

check_case(string_to_check1)
check_case(string_to_check2)
check_case(string_to_check3)