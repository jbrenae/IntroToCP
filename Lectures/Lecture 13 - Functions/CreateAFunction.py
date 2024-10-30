# Creating a function in Python is a straightforward process that allows you to 
# encapsulate a block of code and reuse it whenever needed. 
# 
# Here’s a step-by-step guide:

# Steps to Create a Function in Python:

#   01. Define the Function: Use the def keyword, followed by the function name and parentheses.
#       If the function takes parameters, they go inside the parentheses.

def function_name(parameters):
    # Code block

#   02. Add Parameters (Optional): Functions can accept parameters to make them more flexible.

def greet(name):
    print(f"Hello, {name}!")

#   03. Write the Function Code: Indent the code inside the function to define what it does.

def greet(name):
    print(f"Hello, {name}!")

#   04. Return a Value (Optional): If your function needs to return a result, use the return statement.

def add(a, b):
    return a + b

# 05. Call the Function: To use the function, call it by its name and pass any required arguments.

greet("Alice")
result = add(5, 3)
print(result)

# Summary

# To create a function in Python, you:

# Define it with def and a name.

# (Optional) Add parameters to it.

# Write the code that the function should execute.

# (Optional) Return any results.

# Call the function to use it.