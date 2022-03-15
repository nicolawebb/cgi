from fileinput import filename
import os

#path to text file
# file_name = 'reading and writing files/data.txt'

# #read file
# read_file = open(file_name, 'r')
# for line in read_file:
#     print(line)
# read_file.close()

# #append line to file
# append_file = open(file_name, 'a')
# append_file.write("MNO345, Research Methods, E17, 25")
# append_file.close()

# #write line to file - overrides existing file content
# file_name2 = 'reading and writing files/deletecontents.txt'
# write_file = open(file_name2, 'w')
# write_file.write(":(")
# write_file.close()

#delete a file
file_name3 = 'reading and writing files/delete.txt'
if os.path.exists(file_name3):
    os.remove(file_name3)
else:
    print("The file does not exist")