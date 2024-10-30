#
#
# Types of Parameter Passing

# 1. Positional Arguments
#      - Arguments that are passed to a function in the correct positional order

def add(a, b):
    return a + b

result = add(3, 5)  # Positional arguments: 3 is 'a', 5 is 'b'
print(result)  # Outputs: 8

# 2. Keyword Arguments
#       - Arguments passed with the name of the parameter.

def greet(name, message):
    print(f"{message}, {name}!")

greet(name="Bob", message="Good morning")  # Outputs: Good morning, Bob!

# 3. Default Arguments
#       - Parameters that assume a default value if a value is not provided.

def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Alice")  # Uses default message, Outputs: Hello, Alice!
greet("Bob", "Good evening")  # Overrides default, Outputs: Good evening, Bob!

# 4. Variable-Length Arguments
#       Allows a function to accept an arbitrary number of arguments.

#       \args*: Non-keyword variable-length arguments.

#       \\kwargs**: Keyword variable-length arguments.

def sum_all(*args):
    return sum(args)

result = sum_all(1, 2, 3, 4)
print(result)  # Outputs: 10

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=25)  # Outputs: name: Alice age: 25

# Example Combined:

def describe_pet(pet_name, animal_type="dog", *args, **kwargs):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")
    if args:
        print("Additional info:", args)
    if kwargs:
        print("Details:", kwargs)

describe_pet("Willie")
describe_pet("Harry", "hamster")
describe_pet("Rocky", "dog", "brown fur", "small size", age=5, favorite_food="bones")

# Summary: 

# Positional Arguments: Passed in order.

# Keyword Arguments: Passed with parameter names.

# Default Arguments: Have default values.

# Variable-Length Arguments: Accept multiple values using *args and **kwargs.