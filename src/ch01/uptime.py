import subprocess

def get_linux_uptime():
    try:
        # Run the 'uptime' command and capture the output
        uptime_output = subprocess.check_output(["uptime"]).decode("utf-8")
        
        # Extract the uptime information from the output
        uptime_info = uptime_output.split(",")[0].strip()
        
        return uptime_info
    except Exception as e:
        return f"Error: {e}"

# Get and print the server uptime
uptime = get_linux_uptime()
print(f"Server Uptime: {uptime}")
