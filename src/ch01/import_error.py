try:
    # Attempt to import a non-existent module
    import nonexistent_module

except ImportError as e:
    # Handle ImportError (e.g., module not found or import error)
    print(f"ImportError: {e}")
