# With the continue statement we can stop the current iteration, and continue with the next.

# Example: Continue to the next iteration if i is 3:

i=1

while i < 6:
    if i == 3:
        i += 1
        continue
    print(i)
    
print(i)
i += 1