try:
    # Attempt to access a non-existent key in a dictionary
    my_dict = {"name": "John", "age": 30}
    value = my_dict["nonexistent_key"]

except KeyError as e:
    # Handle KeyError (e.g., attempting to access a non-existent key)
    print(f"KeyError: {e}")