import urllib.request
import json
import getpass

#url = input('Enter a URL: ')
HEROKU_URL = 'https://shrouded-garden-8170.herokuapp.com/'

USER = ''
PASS = ''

def authenticate():
    USER = input('username: ')
    PASS = getpass.getpass('password: ')

authenticate()

filename, _ = urllib.request.urlretrieve(url) # download the file and keep its name
j = json.load(open(filename))

print(j)


