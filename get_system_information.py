import platform
import psutil
import socket

def get_system_information():
    """
    Retrieves system information such as operating system, architecture, hostname, CPU usage, memory usage,
    IP address, and number of open ports.

    Prints the system information to the console and returns it as a dictionary.

    Returns:
        dict: A dictionary containing system information.
    """
    def get_number_of_open_ports():
        """
        Retrieves the number of open ports on the system.

        Returns:
            int: The number of open ports.
        """
        open_ports = psutil.net_connections()
        return len(open_ports)

    # CPU and memory usage
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    
    # IP address
    ip_address = socket.gethostbyname(socket.gethostname())
    
    # Number of open ports
    open_ports = get_number_of_open_ports()

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

    # Print system information to console
    
    print(system_info) 
