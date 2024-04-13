import platform
import psutil
import socket
import subprocess

def get_system_information():
    """
    Retrieves system information such as operating system, architecture, hostname, CPU usage, memory usage,
    IP address, and number of open ports.

    Returns:
        dict: A dictionary containing system information.
    """
    # CPU and memory usage
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    
    # IP address
    ip_address = socket.gethostbyname(socket.gethostname())
    
    # Number of open ports
    open_ports = len(subprocess.check_output(["netstat", "-an"]).splitlines())

    system_info = {
        "Operating System": platform.system(),
        "OS Release": platform.release(),
        "OS Version": platform.version(),
        "Machine Type": platform.machine(),
        "Processor": platform.processor(),
        "Hostname": platform.node(),
        "CPU Usage (%)": cpu_usage,
        "Memory Usage (%)": memory_usage,
        "IP Address": ip_address,
        "Number of Open Ports": open_ports
    }
    return system_info

# Test the function
system_info = get_system_information()
for key, value in system_info.items():
    print(f"{key}: {value}")
