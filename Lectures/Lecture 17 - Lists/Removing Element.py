#
#
# 1. Using remove(): Remove the first occurence of a specified value (Raises Value Error if not found)

my_list = [1,2 , 3, 4]
my_list.remove(2)
print(my_list)

# 2. Using pop(): Removes an element at a specified index and returns it (raises IndexError if the index is out of range)

my_list = [1, 2, 3, 4]
removed_element = my_list.pop(1)
print(removed_element)
print(my_list)

# 3. Using del: Deletes as element at a specified index or deletes the entire list

my_list = [1, 2, 3, 4]
del my_list[1]
print(my_list)

# 4. Using List Comprehension: Create a new list without the element you want to remove

my_list = [1, 2, 3, 4]
my_list = [x for x in my_list if x != 2]
print(my_list)
