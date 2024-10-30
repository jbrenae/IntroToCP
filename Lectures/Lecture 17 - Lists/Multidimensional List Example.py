# Programming Challenge
#
# Given a list in the form: 

# [["CHM 2024","Chemistry 1"3],
# ["ENG 101",English 101",3],
# ["PHY 302",Physics 2",3]]

# Do the following: 

# Print each course number
# Print each course name
# Print each course credits
# Sum the course credits

courses = [["CHM 2024","Chemistry 1",3],
["ENG 101", "English 101",3],
["PHY 302","Physics 2",3]]

print(courses)
print()
for index in range(3):
    print(courses[index][0])
print()
for index in range(3):
    print(courses[index][1])
print()

sum = 0
for index in range(3):
    print(courses[index][2])
    sum = sum + courses[index][2]
print()
print("Sum of course credits: ",sum)

