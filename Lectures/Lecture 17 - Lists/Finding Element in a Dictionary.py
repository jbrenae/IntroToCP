#
#
# 1. Using in: Check if a key excists in the dictionary

my_dict = {'a': 1, 'b': 2}
if 'b' in my_dict:
    print("Key 'b' found!")

# 2. Accessing values: Use the key to get its corresponding value

my_dict = {'a': 1, 'b': 2}
value = my_dict.get('b')
print(value)