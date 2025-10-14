# Q4 WAP to find mean, median & mode of given number (take user input)

from collections import Counter
import statistics

numbers_str = input("Enter numbers separated by spaces: ")
numbers = [int(num) for num in numbers_str.split()]

# Calculate the mean
mean = statistics.mean(numbers)
print(f"Mean: {mean}")

# Calculate the median
median = statistics.median(numbers)
print(f"Median: {median}")

# Calculate the mode
# Use Counter to find the frequency of each number
counts = Counter(numbers)

# Find the number(s) with the highest frequency
max_freq = max(counts.values())
mode = [num for num, freq in counts.items() if freq == max_freq]

print(f"Mode: {mode}")