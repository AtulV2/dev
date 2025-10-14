# Q2 WAP to count no of vovels in a string (take user input)

str = input("Enter a string: ")
vovels = "aeiouAEIOU"
count = 0
for char in str:
    if char in vovels:
        count += 1
print(f"No of vovels in {str} is {count}")