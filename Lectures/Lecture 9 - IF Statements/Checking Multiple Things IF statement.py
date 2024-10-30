# Checking  Multiple Things IF statement

# Problem: I am taking CGS 2060 and it meets on Mondays and Wednesdays.
# I want to create a Python program to remind me to go to class if today is 
# either Monday or Wednesday:

dayOfWeek = "Monday"
dayOfWeek = "Wednesday"

if (dayOfWeek == "Monday") or (dayOfWeek == "Wednesday"):
    print("Go to class!")

# If I only want to go to class on Monday if I have my homework done? AND

if(dayOfWeek == "Monday") and (homeworkDone == True):
    print("Go to class!")