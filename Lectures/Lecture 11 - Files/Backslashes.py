#
#
# When you specify a file name as a string literal, and the name contains backslash characters
#   (as in a Windows file name), you musy supply each backslash twice:

infile = open("c:\\homework\\input.txt", "r")


# A single backslash is an escape character that is combined with the 
#   following character to form a special meaning, such as \n for a newline character

#  \\ denotes a single backslash
