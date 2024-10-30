#Formatted output

name = "John Smith"
televisions = 27

#First Way 

print(" I am "+name+" I own "+str(televisions)+" televisions and I am "+str(4/5)+" of the way through college.")
print()

#Second Way
print(" I am {0} I own {1} televisions and I am {2} of the way through college.".format(name, televisions, 4/5))
print()

#Third Way/Flippped

print(" I am {1} I own {2} televisions and I am {0} of the way through college.".format(name, televisions, 4/5))
print()

#---------------------#

print("{0:12d}".format(1000))

# When printing integers you specify a "d" that includes the number of spaces you would like to use to print the number
# to add a comma printed after every 3rd number you include a ","

print("{0:12,d}".format(1000))

# Printing floating point numbers you specify with an "f"

# Include the # of spaces you would like to use to print the number

print("{0:8f}".format(1.2345))

# To have a comma printed after every 3 digits include a ","

print("{0:8,f}".format(1000.23))

# The number of digits that you want printed after the "."

print("{0:8,.2f}".format(1000.2345))

# 0:8,.2f <--Means I want to start at location zero, I want to print 8 characters, turn on the commas, and .2 puts two characters after the decinmal point