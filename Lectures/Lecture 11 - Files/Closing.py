# Closing a File

# If the output file already exists, it is emptied and the new data is written into it. 
# If the file does not exist an empty one is created. 

# Be sure to CLOSE the file using the close method:

infile.close()
outfile.close()

# If program exits without closing a dile that was opened for writing some of the 
# output may NOT be written to the disk file. 

# If file is closed it can NOT be reused again until it is reopened. 