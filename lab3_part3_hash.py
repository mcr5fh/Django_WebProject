import os
import os.path
import json
from Crypto.Hash import SHA256

the_list = json.load(open('file_info.txt'))

for s in the_list[1]:
    #lines = len(open(s).readlines())
    hashed = SHA256.new(str.encode(str(open(s).readlines()))).hexdigest()
    if hashed != the_list[1][s]:
        print(s + ' does not match')
