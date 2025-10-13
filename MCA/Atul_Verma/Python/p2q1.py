# Write a Python program to reverse only the vowels in a given string, keeping other characters in their original positions.

# input_str = input("Enter a string: ")
input_str = 'a1e2i3o4u5a6'

list_str = list(input_str)

vowels = 'aeiouAEIOU'

vowel_list = []

for char in list_str:
    if char in vowels:
        vowel_list.append(char)
    

# Reverse the vowel list
vowel_list = vowel_list[::-1]

result = list_str
for i in range(len(list_str) -1):
    
    if result[i] in vowels:
        result[i] = vowel_list[(len(vowel_list) - 1) - i]

        
print("String with reversed vowels:", result)




# input_str = 'a1e2i3o4u5a6'

# list_str = list(input_str)

# vowels = 'aeiouAEIOU'

# vowel_list = []

# # Collect vowels
# for char in list_str:
#     if char in vowels:
#         vowel_list.append(char)

# # Reverse the vowel list
# vowel_list = vowel_list[::-1]

# # Replace vowels in original positions
# vowel_index = 0
# for i in range(len(list_str)):
#     if list_str[i] in vowels:
#         list_str[i] = vowel_list[vowel_index]
#         vowel_index += 1

# print("String with reversed vowels:", ''.join(list_str))
