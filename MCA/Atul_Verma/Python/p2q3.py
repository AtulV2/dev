# Q3 Given a list of items (possibly with duplicates), write a program that removes duplicates and displays the sorted list.

input_str = input("Enter the list of items seperated by spaces: ") # 'apple banana apple orange banana'
list_items = input_str.split()
set_items = set(list_items)
print(f'Unique & Sorted Items: {sorted(set_items)}')
