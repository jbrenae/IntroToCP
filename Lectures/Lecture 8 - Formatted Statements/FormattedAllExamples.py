# Python Program showing a use of format() method

# Combining positional and keyword arguments
print("For lunch I like to eat {0}, {1}, and {other}.".format('cake', 'pie', other ='hotdogs'))

# Using format() method with number
print("Students: {0:d}, Average Score: {1:f}".format(12, 78.546))

# Changing positional argument
print("Second argument:{1:3d}, First one:{0:7.2f}".format(47.42,11))

print("Bottles of beer:{a:5d}, Hours to drink:{p:8.2f}".format(a = 453, p = 59.058))

# The brackets and characters within the { } are replaced with objects passed into the format() method.

# A number in the brackets can be used to refer to the position of the object passed into the format() method.