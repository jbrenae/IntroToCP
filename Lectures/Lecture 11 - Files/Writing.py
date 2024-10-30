# Python has TWO different ways to write to a file.
    # 1. Write
    # 2. Print
# You can write text to a file that has been opened for writing. 
#
# Example:  outfile.write("Hello, World!\n")
# 
# When writing text to an output file using write you must 
# explicitly write the newline character to start a new line.           
#
# Can write FORMATTED strings to a file with the write method.
# 
# Example: 
count = 123
total = 576.42865

outfile = open("1103 output.txt", "w")
outfile.write("Hello, World!\n")
outfile.write("Number of entries: {0:d}\nTotal: {1:8.2f}\n".format(count, total))

# outfile.close()
# demo overwriting of output file

print("All Done!")

# --------- Writing WITH a PRINT statement --------- #
 
# The print FUNCTION adds a newline character at the end of its 
#   output to start a new line automatically. 
#
# Supply the file object as an argument with the name, file, as follows:

print("Hello, World!", file=outfile)

# If you don't want a newline, use the end argument. 

print("Total: ", end="", file=outfile)

##### EXAMPLE #####

count = 123
total = 576.42865

outfile = open("1103 output.txt", "w")
outfile.write("Hello, World!\n")
outfile.write("Number of entries: {0:d}\nTotal: {1:8.2f}\n".format(count, total),file=outfile)

outfile.close()
print("All Done!")