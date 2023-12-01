try:
    # Attempt to open a non-existent file for reading
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()

except IOError as e:
    # Handle IOError (e.g., file not found or permission issues)
    print(f"IOError: {e}")
