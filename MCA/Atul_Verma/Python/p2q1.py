# Write a Python program to reverse only the vowels in a given string, keeping other characters in their original positions.

input_str = input("Enter a string: ") # eg: 'a1e2i3o4u5a6'

list_str = list(input_str)
vowels = 'aeiouAEIOU'
v_list = []

for char in list_str:
    if char in vowels:
        v_list.append(char)
    
# Reverse the vowel list
v_list_rev = v_list[::-1]

result = list_str
vowel_index = 0
for i in range(len(list_str)):
    if list_str[i] in vowels:
        result[i] = v_list_rev[vowel_index]
        vowel_index += 1
    else:
        result[i] = list_str[i]

print("String with reversed vowels:", ''.join(result)) 



