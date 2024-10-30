# How Return Values Work:
# Define a Function: Use the def keyword to define a function.

# Compute a Value: Perform calculations or operations inside the function.

# Return the Value: Use the return keyword to send the value back to the caller.

def add(a, b):
    return a + b

# When you call this function, it will compute the sum of a and b and return the resul

# ------- Using Return Values: 

result = add(5, 3)
print("The sum is:", result)

# ------- Multiple Return Values:

# A function can also return multiple values using tuples.

def get_coordinates():
    x = 10
    y = 20
    return x, y

x, y = get_coordinates()
print("X:", x)
print("Y:", y)

# No Return Value:
