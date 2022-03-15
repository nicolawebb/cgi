from fileinput import filename
import re

file_name = 'data.txt'
file = open(file_name, 'r')
count = 1
for line in file.readlines():
    # re.split(line, ',')
    print(line)
    # print(count , line)
    # count +=1