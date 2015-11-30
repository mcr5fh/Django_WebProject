import urllib.request
import json
import getpass

#url = input('Enter a URL: ')
#DEPLOY_URL = 'https://shrouded-garden-8170.herokuapp.com/'
DEPLOY_URL = 'http://0.0.0.0:5000/'

USER = ''
PASS = ''

def authenticate():
    USER = input('username: ')
    PASS = getpass.getpass('password: ')

#authenticate()
url = DEPLOY_URL + 'api/list'

filename, _ = urllib.request.urlretrieve(url) # download the file and keep its name
reports = json.load(open(filename))

#print(reports)

i = 0
for report in reports:
    print(str(i) + ': ' + report['short'] + ' (' + report['url'].split('/')[-1] + ')')
    i += 1

which = input('select a report to download (0-' + str(i-1) + '): ')
