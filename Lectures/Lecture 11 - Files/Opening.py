# Opening Files:
# Mode: Specifies what operations we intend to perform on a file

#           R - Read: Get the name of the file and make it a variable. (This will read the file) or
#                     if the file name is stored in a different directory from your python program file,
#                     state the file name preceded by the directory path.

#           W - Write: Provide the name of he file if its in same directory or provide name followed by dircetory path
#                      Important: If the file does not exist, python will create it for you. If it DOES exist Python will 
#                                 DELETE it and then create a new version for you - whatever is in the file will be lost forever. 

#           A - Append: Keeping the original file and adding to it. 

infile = open("input.txt",  "r")
outfile1 = open("input.txt",  "w")
outfile2 = open("input.txt",  "a")

print("infile: ",infile)
print() ## ^^ Reads the data
print("outfile1: ",outfile1)
print() ## ^^ Writes the data
print("outfile2: ",outfile2)
print("All Done!")