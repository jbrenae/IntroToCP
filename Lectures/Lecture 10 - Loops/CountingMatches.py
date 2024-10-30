# Counting Matches

text = "The rain in Spain falls mainly on the plain"

uppercase = 0
for char in text:
    if char.isupper():
        uppercase = uppercase + 1
print("# uppercase characters = ",uppercase)
print()

vowels = 0
for char in text:
    if char.lower() in "aeiou":
        vowels = vowels + 1
print("# vowels in text = ",vowels)

