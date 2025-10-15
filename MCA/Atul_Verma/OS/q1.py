# Write a python program to display monitor network statistics bytes sent/received

import psutil

net_io = psutil.net_io_counters()
print(f"Bytes Sent: {net_io.bytes_sent/1024**2:.2f} MB")
print(f"Bytes Sent: {net_io.bytes_recv/1024**2:.2f} MB")

# Output:
# Bytes Sent: 180.74 MB
# Bytes Sent: 4655.46 MB