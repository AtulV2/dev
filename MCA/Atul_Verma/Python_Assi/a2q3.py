# 8. Write a program that reads a text file and counts the number of lines, words, and characters

with open('text1.txt', 'r') as file:
    lines = file.readlines()  

# Count the number of lines
num_lines = len(lines)

num_words = 0
num_char_with_spaces = 0
num_char = 0
num_spaces = 0


for line in lines:
    # Count words in the current line by splitting on whitespace
    words_in_line = line.split()
    num_words += len(words_in_line)
    
    
    num_spaces = line.count(' ')
    num_char_with_spaces += len(line)
    
# Count characters excluding spaces and newline characters
num_char = num_char_with_spaces - num_spaces - (num_lines - 1)
print("Lines:", num_lines)
print("Words:", num_words)
print("Characters:", num_char)
