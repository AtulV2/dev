# Accept a list of students and their marks as tupes. Display the name of the student with the highest marks

input_list = eval(input("Enter the list of ('name', marks) tuples:\n")) # [('Alice', 88), ('Bob', 92), ('Carol', 79)]


highest_marks = 0
highest_student = 0

for tup in input_list:
    if tup[1] > highest_marks:
        highest_marks = tup[1]
        highest_student = tup[0]

print("Student with the highest marks:", highest_student)



