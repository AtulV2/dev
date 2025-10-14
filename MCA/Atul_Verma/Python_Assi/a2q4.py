# 9. Read a sentence and display how many times each word appears, ignoring case and punctuation.

# input_str = input("Enter text: ")
input_str = 'Rain rain go away, come again another day.'

input_str = input_str.lower()
char_dict = {}

for char in input_str.split():
    if char in char_dict:
        char_dict[char] += 1
    else:
        char_dict[char] = 1

print(char_dict)