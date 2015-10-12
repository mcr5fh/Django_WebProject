import os
import os.path
import json

the_list = json.load(open('file_info.txt'))

for s in the_list[1]:
    lines = len(open(s).readlines())
    if lines != the_list[1][s]:
        print(s + ' does not match')
