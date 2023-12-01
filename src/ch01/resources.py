import psutil

def get_disk_usage():
    try:
        # Get disk usage information
        disk_usage = psutil.disk_usage('/')
        
        # Extract and format relevant information
        total_size_gb = round(disk_usage.total / (1024 ** 3), 2)
        used_size_gb = round(disk_usage.used / (1024 ** 3), 2)
        free_size_gb = round(disk_usage.free / (1024 ** 3), 2)
        usage_percentage = disk_usage.percent

        return {
            'total_size_gb': total_size_gb,
            'used_size_gb': used_size_gb,
            'free_size_gb': free_size_gb,
            'usage_percentage': usage_percentage
        }
    except Exception as e:
        return f"Error: {e}"

def get_memory_usage():
    try:
        # Get memory usage information
        memory = psutil.virtual_memory()
        
        # Extract and format relevant information
        total_memory_gb = round(memory.total / (1024 ** 3), 2)
        used_memory_gb = round(memory.used / (1024 ** 3), 2)
        free_memory_gb = round(memory.available / (1024 ** 3), 2)
        usage_percentage = memory.percent

        return {
            'total_memory_gb': total_memory_gb,
            'used_memory_gb': used_memory_gb,
            'free_memory_gb': free_memory_gb,
            'usage_percentage': usage_percentage
        }
    except Exception as e:
        return f"Error: {e}"

# Get and print disk usage
disk_info = get_disk_usage()
print("Disk Usage:")
print(f"Total: {disk_info['total_size_gb']} GB")
print(f"Used: {disk_info['used_size_gb']} GB")
print(f"Free: {disk_info['free_size_gb']} GB")
print(f"Usage Percentage: {disk_info['usage_percentage']}%")

# Get and print memory usage
memory_info = get_memory_usage()
print("\nMemory Usage:")
print(f"Total: {memory_info['total_memory_gb']} GB")
print(f"Used: {memory_info['used_memory_gb']} GB")
print(f"Free: {memory_info['free_memory_gb']} GB")
print(f"Usage Percentage: {memory_info['usage_percentage']}%")
