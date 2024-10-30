# To read a line of text from a file, call the readline method with the fole object that was returned
#   when you opened the file. 

line = infile.readline()

#   When a file is first opened, an input marker is positioned at the 
#   beginning of the file. 

#   The readline method read the text, starting at the CURRENT position and continuing until 
#   the end of the line is encountered. The input marker is then MOVED to the start of the next line. 

#   Readline method can ONLY contain strings.

#   Reading Data & Loading Input

#   Example:

infile = open("1101 input.txt", "r")

line = infile.readline()
print(line)

line = int(infile.readline())
print(line, line+1)

# If the file contains numerical data you HAVE to convert 
#   the strings to a numberical value using int or float funtion.