# 7. Given a list of employee records as dictionaries, sort them by salary and display the sorted list.

# employees = eval(input("Enter the list of dictionary : \n"))

employees = [{"name": 'John', "salary": 45000}, {"name": 'Mary', "salary": 52000}, {"name": 'Alex', "salary": 48000}]

# Sort the list of dictionaries by the 'salary' key using a lambda function
sorted_employees = sorted(employees, key=lambda x: x['salary'])

print("Sorted by Salary:", sorted_employees)


