import re

###========SEARCH==========###
test_string = 'python'

##with python
starts_with = test_string.startswith('p')
ends_with = test_string.endswith('n')
if starts_with and ends_with:
    print("Search successful.")
else:
  print("Search unsuccessful.")	

##with regex
pattern = '^p....n$'
result = re.search(pattern, test_string)
if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	


###========FIND ALL==========###
test_string = "Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself."

##with python
idx = 0
while idx < len(test_string):
        idx = test_string.find('Sith', idx)
        if idx == -1:
            break
        print('Sith at:', idx)
        idx += 1

##with regex
x = re.findall("Sith", test_string)
print(x)


###========SPLIT==========###
test_string = "The rain in Spain"

##with python
split_string = test_string.split(" ")
print(split_string)

##with regex
split_string = re.split("\s", test_string)
print(split_string)
