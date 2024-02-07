import psutil
import datetime
import time
import database_operations


def start_data_capture(con, interval):
    while True:
        image = get_processes()
        now = datetime.now()

        database_operations.db_insert(con, 'Screenshots', {image, now})

        time.sleep(interval)


def get_processes():
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

    return processes


def compare_lists(first_list, second_list):
    stopped = []
    new = []

    # Find stopped processes
    for process in first_list:
        if process not in second_list:
            stopped.append(process)

    # Find new processes
    for process in second_list:
        if process not in first_list:
            new.append(process)

    return {'stopped': stopped, 'new': new}


# print(get_processes())
a = get_processes()
print("get next")
time.sleep(30)
print("getting next")
b = get_processes()
print(a)
print(b)
print(compare_lists(a, b))
