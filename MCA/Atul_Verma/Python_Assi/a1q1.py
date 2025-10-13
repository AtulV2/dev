# 6. Write a program to search for an item in a user-provided list and display the position if found, otherwise print “Item not found.”

input_str = input("Enter the list seperated by space: ")
input_list = input_str.split()
item = input("Enter the item to search: ")
position = None

for index in range(len(input_list)):
    if input_list[index] == item:
        position = index + 1  
        break

if position is not None:
    print("Item found at position", position)
else:
    print("Item not found.")
