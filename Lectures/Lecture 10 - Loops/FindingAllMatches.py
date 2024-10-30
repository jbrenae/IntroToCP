# Finding all matches

sentence = input("Enter a sentence: ")
for i in range(len(sentence)):
    if sentence[i].isupper():
        print("{0:2d}:{1}".format(i,sentence[i]))