"""
Getting a System information.
----------------------------
info:
    1. Operating system - info
    2. Processor - info
    3. Memory - info
    4. Disk - info
    5. Network - info

Created By `Muhammed Alkohawaldeh`
Date `8/2/2023`
"""
import platform
import psutil

# Get the operating system name
os_name = platform.system()

# Get the processor information
processor = platform.processor()

# Get the amount of available memory
memory = psutil.virtual_memory()
memory_total = f"{memory.total / 1073741824:.2f} GB"
memory_available = f"{memory.available / 1073741824:.2f} GB"
memory_used = f"{memory.used / 1073741824:.2f} GB"
memory_percent = f"{memory.percent}%"

# Get the disk usage information
disk = psutil.disk_usage("/")
disk_total = f"{disk.total / 1073741824:.2f} GB"
disk_used = f"{disk.used / 1073741824:.2f} GB"
disk_free = f"{disk.free / 1073741824:.2f} GB"
disk_percent = f"{disk.percent}%"

# Get the network information
net_io = psutil.net_io_counters()
bytes_sent = f"{net_io.bytes_sent / 1073741824:.2f} GB"
bytes_recv = f"{net_io.bytes_recv / 1073741824:.2f} GB"
packets_sent = f"{net_io.packets_sent}"
packets_recv = f"{net_io.packets_recv}"

# Display the system information
print(f"Operating system: {os_name}")
print(f"Processor: {processor}")
print("Memory:")
print(f"  Total: {memory_total}")
print(f"  Available: {memory_available}")
print(f"  Used: {memory_used}")
print(f"  Percentage used: {memory_percent}")
print("Disk:")
print(f"  Total: {disk_total}")
print(f"  Used: {disk_used}")
print(f"  Free: {disk_free}")
print(f"  Percentage used: {disk_percent}")
print("Network:")
print(f"  Bytes sent: {bytes_sent}")
print(f"  Bytes received: {bytes_recv}")
print(f"  Packets sent: {packets_sent}")
print(f"  Packets received: {packets_recv}")
