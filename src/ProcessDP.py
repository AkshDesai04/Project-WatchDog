import psutil

processes = []

# Iterate over all running processes
for proc in psutil.process_iter(['pid', 'name']):
    try:
        # Get process info as a named tuple
        process_info = proc.info
        processes.append(process_info)
        # Extract process ID and name
        pid = process_info['pid']
        name = process_info['name']

        # Print PID and name
        # print(f"PID: {pid} Name: {name}")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # Handle exceptions that can occur while getting process info
        pass
    # print("Done")

print(processes)