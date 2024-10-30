# When creating w/ vairables you can replace numbers that are being used yo indicate locations

# Step 1: Start by assigning a value to a variable WITHIN the format statement:
numStudents = 55
numTeachers = 2

# Step 2: encapulate the vairable name insude a set of {} INSIDE of the string that you want to print

{numStudents}

# Example 

print("The class has {numStudents} and {numTeachers}.".format(numStudents = 55, numTeachers = 2))
