#
# 
# Using the copy() Method
# This method creates a shallow copy of the list. 
# A shallow copy means it creates a new list object but does not 
# create copies of the objects contained within the original list.


original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy()

print("Original list:", original_list)  # Output: [1, 2, 3, 4, 5]
print("Copied list:", copied_list)      # Output: [1, 2, 3, 4, 5]

# 1. Using List Slicing
#    This also creates a shallow copy of the list.

original_list = [1, 2, 3, 4, 5]
copied_list = original_list[:]

print("Original list:", original_list)  # Output: [1, 2, 3, 4, 5]
print("Copied list:", copied_list)      # Output: [1, 2, 3, 4, 5]

# 2. Using the list() Constructor
#    This is another way to create a shallow copy of the list.

original_list = [1, 2, 3, 4, 5]
copied_list = list(original_list)

print("Original list:", original_list)  # Output: [1, 2, 3, 4, 5]
print("Copied list:", copied_list)      # Output: [1, 2, 3, 4, 5]

# 3. Using the copy Module for a Deep Copy
# If you need to copy nested lists or complex objects (where changes to the copied list should not affect the original list)
# you need a deep copy. This creates a new object and recursively copies all objects found in the original list.

import copy

original_list = [1, 2, [3, 4], 5]
copied_list = copy.deepcopy(original_list)

print("Original list:", original_list)  # Output: [1, 2, [3, 4], 5]
print("Copied list:", copied_list)      # Output: [1, 2, [3, 4], 5]


# Summary:

# Shallow Copy:
#   - copy() method

# Deep Copy:
#   - copy.deepcopy() from the copy module