# How to Return Multiple Values
# Use a Tuple: A tuple is a simple way to return multiple values.
# You just separate them with commas in the return statement.

def get_stats(numbers):
    total = sum(numbers)
    length = len(numbers)
    average = total / length
    return total, length, average

# Capture the Returned Values: When you call the function, 
# you can capture the returned values into separate variables.

total, length, average = get_stats([1, 2, 3, 4, 5])
print("Total:", total)
print("Length:", length)
print("Average:", average)

# This will output: Total: 15
#                   Length: 5
#                   Average: 3.0

# Practical Example

#Let’s say we have a function that calculates the minimum and maximum values from a list.


def find_min_max(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    return min_value, max_value

# When you call this function, you can capture both values:

min_val, max_val = find_min_max([3, 1, 4, 1, 5, 9, 2])
print("Min value:", min_val)
print("Max value:", max_val)

# This will output: Min value: 1
#                   Max value: 9


# Using with Data Structures:
# You can also return more complex data structures. 
# 
# For example, returning a list or a dictionary along with other values:


def analyze_text(text):
    word_count = len(text.split())
    char_count = len(text)
    frequency = {word: text.split().count(word) for word in set(text.split())}
    return word_count, char_count, frequency

# When you call this function, you can get all three values:

words, characters, freq = analyze_text("hello world world")
print("Words:", words)
print("Characters:", characters)
print("Frequency:", freq)

# This will output: Words: 3
#                   Characters: 17
#                   Frequency: {'hello': 1, 'world': 2}

# Summary

# Use a Tuple: Return multiple values separated by commas.

# Capture Values: Assign the returned values to separate variables.

# Complex Structures: Return lists, dictionaries, or other structures if needed.

# Using multiple returns makes your functions more flexible and powerful,
# allowing them to provide all the necessary results in one go. Need to see more examples or dive into a specific use case?