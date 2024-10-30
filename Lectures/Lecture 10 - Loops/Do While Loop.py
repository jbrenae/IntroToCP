# Do While Loop
#                   i = 10
#                   keepCounting = True

# Initialization:
#   i is set to 10. This variable will be used as the countdown number.
#   keepCounting is a boolean variable initialized to True, which controls the while loop.

#                   while (keepCounting):

# While Loop: 
#   This line starts a loop that will continue executing as long as keepCounting is True.

    #               print("T minus {0} and counting".format(i))


# Printing the countdown:
#   Inside the loop, this line prints the current value of i in the format "T minus {i} and counting". 
#   The {0} is a placeholder that gets replaced by the value of i using the format method.
    
#                   i = i - 1

# Decrementing i:
# This line decreases the value of i by 1. So, if i starts at 10, it will become 9 after the first iteration.

#                   if (i < 0):
#                   keepCounting = False

# Stopping Condition:
#   This if statement checks if i is less than 0. If it is, it sets keepCounting to False, which will stop 
#   the while loop in the next iteration.


#                   print("All Done!")

#   Final Message:
#       Once the loop exits (when i goes below 0), this line executes and prints "All Done!" to indicate that the 
#       countdown has finished.


# Code put together: 

i = 10
keepCounting = True

while (keepCounting):
    print("T minus {0} and counting".format(i))
    i = i - 1
    if (i < 0):
        keepCounting = False

print("All Done!")