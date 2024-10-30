# AHPA #17: The Blizzard Problem
#
# 1. Print out the lists: one item per line.
#
# 2. In the Candy Cravers list, print the Heath item’s location.
#
# 3. In the Classic Creations list, print the Royal Rocky Road item.
#
# 4. Add a new Classic Creation: "red licorice". 
#
# 5. Print new list.
#
# 6. Remove the Heath Blizzard from Candy Cravers. 
#
# 7. Print new list.
#
# 8. Combine the lists and print on one line
#
# 9. Print a count of the total number of treats provided
#
# Student Name: Jalisa Greene
#

candyCravers = ["Reese’s Peanut ButterCup", "Butterfinger", "Oreo", "Heath", "M&M’s"]

classicCreations =["Banana Split", "Salted Caramel Truffle", "M&M’s Peanut Butter Monster Cookie", 
"Georgia Mud Fudge", "Double Fudge Cookie Dough", "Chocolate Xtreme",
"Peanut Butter Cookie Dough Smash", "Chocolate Chip Cookie Dough", "Royal Rocky Road", "Chocolate Covered Strawberry", "Choco Covered Strawberry", "Royal Rocky Road",
"Turtle Pecan Cluster", "Mint Oreo", "Royal New York Cheesecake", "Royal Oreo"]


print()
print("Candy Cravers:")
print()

for candy in candyCravers:
    print(candy)
print()

print("Classic Creations:")
print()

for creations in classicCreations:
    print(creations)
print()

heathLocation = candyCravers.index("Heath")
print("Heath is at location",[heathLocation], "in the Candy Cravers List")
print()

classicCreations.remove("Royal Rocky Road") #-- This was on there twice so I removed one. 
for item in classicCreations:
    if item == "Royal Rocky Road":
        print(item)


print()
classicCreations.append("Red Licorice")
print("New List of Classic Creations: ")
print()

for item in classicCreations:
    print(item)

print()
candyCravers.remove("Heath")
print("Updated Candy Cravers List: ")
print()
for candy in candyCravers:
    print(candy)
print()

lists = candyCravers + classicCreations
print("Classic Candy & Creations: ")
print()
print(", ".join(lists))

print()
sweetsTotal = len(lists)
print("We offer a total of", sweetsTotal, "treats!")
print()