# If the file containes a blank line, then readline returns 
#   a string containing only the newline character "\n"
#
# Reading multiple lines of text from a file is very similar to reading
#   a sequence of values with the input function.

# You repeatedly read a line of text and process it 
#       until the sentinel value is reached:

line = infile.readline()
while (line != ""):
    #Process The Line.
    line = infile.readline()
