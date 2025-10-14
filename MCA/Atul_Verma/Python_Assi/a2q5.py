# 10. Write a Python program that lists all files in a directory and categorizes them by file extension.

import os

# Get all files in the current directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# Dictionary to categorize files by extension
categorized_files = {}

for file in files:
    # Extract file extension
    if '.' in file:
        extension = file.split('.')[-1]
    else:
        extension = ''  # Files with no extension
    
    # Add file to the appropriate category
    if extension not in categorized_files:
        categorized_files[extension] = []
    categorized_files[extension].append(file)

print(categorized_files)
