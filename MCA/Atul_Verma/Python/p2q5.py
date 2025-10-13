# Read data from a CSV file containing employee details (name, department, salary) and display the average salary by department.

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


with open('file1.csv' ,'r') as f:
    reader = csv.DictReader(f)
    dept_salaries = {}
    dept_counts = {}
    
    for row in reader:
        dept = row['department']
        salary = float(row['salary'])

        if dept in dept_salaries:
            dept_salaries[dept] += salary
            dept_counts[dept] += 1
        else:
            dept_salaries[dept] = salary
            dept_counts[dept] = 1

    print("Average Salary by Department:")
    for dept in dept_salaries:
        avg_salary = dept_salaries[dept] / dept_counts[dept]
        print(f"{dept}: {avg_salary:.2f}")
