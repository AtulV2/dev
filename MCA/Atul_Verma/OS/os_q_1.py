import platform

# Get OS name
os_name = platform.system()

# Get OS version
os_version = platform.version()

# Get architecture
architecture = platform.architecture()[0]

# Display results
print("Operating System Name:", os_name)
print("Operating System Version:", os_version)
print("Operating System Architecture:", architecture)
