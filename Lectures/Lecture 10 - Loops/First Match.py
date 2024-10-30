# First Match

found = False
string = "There are 7 days in a week and 30 days in a month."
print(string)

position = 0
while not found and position < len(string):
    if string[position].isdigit():
        found = True
    else:
        position = position + 1

if found:
    print("First digit occurs at position", position)
else:
    print("The string does not contian a digit.")