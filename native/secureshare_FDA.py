import urllib.request, urllib.error
import json
import getpass
import requests

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
#filename = requests.get(
reports = json.load(open(filename))

print('List of reports and (attached files): ')

i = 0
for report in reports:
    print(str(i) + ': ' + report['short'] + ' (' + report['url'].split('/')[-1] + ')')
    i += 1

which = int(input('select a report to download (0-' + str(i-1) + '): '))

download_url = DEPLOY_URL + reports[which]['url']
try: 
    download_filename, _ = urllib.request.urlretrieve(download_url) # download the file and keep its name
    print('downloaded file to ' + download_filename)
except urllib.error.HTTPError:
    print('This report does not contain a file.')
