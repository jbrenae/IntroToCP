# Finding an elemenet in Python also depends on the data structure you're using.
# Here os jpw upi cam do it for lists and dictionaries. 

# 1. Using in: Check if an element exists in a list.

my_list = [1,2,3,4]
if 3 in my_list:
    print("Found #!")

# 2. Using index(): Get the index of an element (will raise a ValueError if not found)

my_list = [1, 2, 3, 4]
index = my_list.index(3)
print(index)

# 3. Using count(): Count occurences of an element

my_list = [1, 2, 2, 3, 4]
count = my_list.count(2)
print(count)