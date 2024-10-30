# 
# You are in the process of creating a calendar program. 
# But its not going very well for you. 

# You've been given the string
# ("Monday", "Tuesday", "Tuesday", "Thursday", "Friday")

# Turn this string into a list

# Append "Saturday" and "Sunday" to the end of the list

# Insert "Wednesday" into the list in the correct position

# Check to make sure that "Friday" is in the list

# Remove the second "Tuesday" from the list. 

                                        # -------------------- Code ---------------------- # 

# Step 1: Convert the string into a list

days = ["Monday", "Tuesday", "Tuesday", "Thursday", "Friday"]

# Step 2: Append "Saturday" and "Sunday"

days.append("Saturday")
days.append("Sunday")

# Step 3: Insert "Wednesday" (between Tuesday and Thursday)

days.insert(days.index("Thursday"), "Wednesday")

# Step 4: Check if "Friday" is in the list

if "Friday" in days:
    print("Friday is in the list.")

# Step 5: Finds the index of the second "Tuesday" and remove it.

first_tuesday_index = days.index("Tuesday") 

# Remove the second occurence by searching for "Tuesday" again after the first

second_tuesday_index = days.index("Tuesday", first_tuesday_index + 1) # - The +1 locates the second occurence of Tuesday which is at index 2. 
days.pop(second_tuesday_index)

# output

print(days)