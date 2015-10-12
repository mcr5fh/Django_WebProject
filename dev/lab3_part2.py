import os
import os.path
import json

the_list = [os.getcwd(), {}]

for f in os.listdir():
    if os.path.isdir(f):
        continue
    lines = len(open(f).readlines())
    the_list[1][f] = lines
     
#print(json.dumps(the_list))
text_file = open('file_info.txt', 'w+')
json.dump(the_list, text_file)
