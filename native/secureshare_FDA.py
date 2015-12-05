import urllib.request, urllib.error
import json
import getpass
import requests
import sys

#url = input('Enter a URL: ')
DEPLOY_URL = 'https://shrouded-garden-8170.herokuapp.com'
#DEPLOY_URL = 'http://0.0.0.0:5000'

USER = input('username: ')
PASS = getpass.getpass('password: ')

url = DEPLOY_URL + '/api/list'

r = requests.get(url, auth=(USER, PASS))

reports = json.loads(r.text)

print('List of reports and (attached files): ')
i = 0
for report in reports:
    print(str(i) + ': ' + report['short'])
    #print(report['short'])
    i += 1

if i <= 0:
    print('No reports.')
    sys.exit(0)
    

which_report = int(input('select a report to download (0-' + str(i-1) + '): '))

dl_report = reports[which_report]
dl_urls = [report['file1'], report['file2'], report['file3'], report['file4'], report['file5']]
dl_urls = filter(lambda x: x != '', dl_urls)
dl_urls = list(map(lambda x: DEPLOY_URL + x, dl_urls))

for dl_url in dl_urls:
    r = requests.get(dl_url)
    filename = dl_url.split('/')[-1]
    with open(filename, "wb") as f:
        f.write(r.content)
    print('downloaded ' + filename)

print('done')
