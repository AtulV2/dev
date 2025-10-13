import csv

list1 = [
    ['name', 'department', 'salary'],
    ['John', 'IT', 50000],
    ['Mary', 'IT', 55000],
    ['Alice', 'HR', 48000],
    ['Bob', 'HR', 52000]
]

with open('file1.csv', 'w') as f:
    write = csv.writer(f)
    write.writerows(list1)