#sk
import os
import os.path
import json
from Crypto.Hash import SHA256

the_list = [os.getcwd(), {}]

for f in os.listdir():
    if os.path.isdir(f):
        continue
    #lines = len(open(f).readlines())
    hashed = SHA256.new(str.encode(str(open(f).readlines()))).hexdigest()
    the_list[1][f] = hashed
     
#print(json.dumps(the_list))
text_file = open('file_info.txt', 'w+')
json.dump(the_list, text_file)
