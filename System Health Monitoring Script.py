import psutil
import logging

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.WARNING, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80.0  # Percentage
MEMORY_THRESHOLD = 80.0  # Percentage
DISK_THRESHOLD = 90.0  # Percentage

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
    return cpu_usage

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High Memory usage detected: {memory_usage}%")
    return memory_usage

def check_disk_space():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"Low Disk Space: {disk_usage}% used")
    return disk_usage

def check_running_processes():
    processes = len(psutil.pids())
    return processes

if __name__ == "__main__":
    cpu = check_cpu_usage()
    memory = check_memory_usage()
    disk = check_disk_space()
    processes = check_running_processes()

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")
    print(f"Running Processes: {processes}")
