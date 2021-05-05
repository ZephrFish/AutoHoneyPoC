#!/usr/bin/env python3
# AutoPoC Generator HoneyPoC ULTIMATE EDITION
#
#
# What This Script Does:
# 1. Stage 1: Poll CVEs from Database URL and then drop them into a list to itterate through and create canary tokens for each CVE
# 2. Stage 2a: Create Git Repo and Push updates to Repo
# 3. Stage 2b: Email User alert that new repo has been created, document the Repo Link, CVEID and CanaryToken ID
# 4. Stage 2c: Create Pastebin Entry with git repo name and CVE information
# 5. Stage 3: Build PoC From Templates, input the CVE and CanaryID to the specific PoC
#
# Tooling Used
# CVE Search: https://github.com/barnumbirr/ares
# Thinkst Canary: https://canary.tools


import smtplib
from ares import CVESearch
import requests
import requests_cache
from collections import namedtuple
import sys
import os 

version = "0.0.1"
WD = os.path.dirname(os.path.realpath(__file__))

# Builds Requests Cache with DB called TrollList - Does Monkey Patching of requests
requests_cache.install_cache(os.path.join(WD, "TrollList"), expire_after=3600)

def banner():
    print("""
    
 __    __                                          _______              ______
|  \  |  \                                        |       \            /      \
| $$  | $$  ______   _______    ______   __    __ | $$$$$$$\  ______  |  $$$$$$\
| $$__| $$ /      \ |       \  /      \ |  \  |  \| $$__/ $$ /      \ | $$   \$$
| $$    $$|  $$$$$$\| $$$$$$$\|  $$$$$$\| $$  | $$| $$    $$|  $$$$$$\| $$
| $$$$$$$$| $$  | $$| $$  | $$| $$    $$| $$  | $$| $$$$$$$ | $$  | $$| $$   __
| $$  | $$| $$__/ $$| $$  | $$| $$$$$$$$| $$__/ $$| $$      | $$__/ $$| $$__/  \
| $$  | $$ \$$    $$| $$  | $$ \$$     \ \$$    $$| $$       \$$    $$ \$$    $$
 \$$   \$$  \$$$$$$  \$$   \$$  \$$$$$$$ _\$$$$$$$ \$$        \$$$$$$   \$$$$$$
                                        |  \__| $$
                                         \$$    $$
                                          \$$$$$$



Automated Fuckery Ultimate Edition
Research Project 
Enjoy!
    """)

# Stage 1: Poll CVEs from Database URL and then drop them into a list to itterate through and create canary tokens for each CVE
def PollCVEs():
    cveSer = CVESearch()
    # Grab last CVE number
    CVEList = cveSer.last('1')
    
 
    # Print out Last output
    # print([Entry['id'] for Entry in CVEList][-1])
    # Return list of values in array
    print([Entry['id'] for Entry in CVEList])
     
    # Iterate through the strings in the array

    canaryurllist = []
    # Creates a name space of the pair of canary url and CVE id
    CVECanaryPair = namedtuple('CVECanaryPair', ['id', 'url'])

    for CVEID in CVEList:
       data = {
           'auth_token': 'KEY',
           'memo': CVEID['id'],
           'kind': 'http'
           }
       response = requests.post('https://SUBDOMAIN.canary.tools/api/v1/canarytoken/create', data=data)
       canaryurl = response.json()['canarytoken']['url']
       
       pair = CVECanaryPair(id=CVEID['id'],url=canaryurl)
       canaryurllist.append(pair)
    print(canaryurllist)

    # To call
    # for pair in canaryurllist:
    #     print(pair.id, pair.url)
    return canaryurllist

# Stage 2a: Create Git Repo and Push updates to Repo
def CreateGitRepo(RepoName):
    # Create Repo and Init it
    global WD
    os.chdir(os.path.join(WD,RepoName))
    os.system('git init')
    os.system('git add README.md')
    os.system(f'git add {RepoName}.sh')
    data = {
        'name': RepoName    
    }
    r=requests.post('https://api.github.com/user/repos', json=data, auth=('USERNAME', 'KEY'))
    os.system('git commit -m "Initial Commit"')
    os.system('git branch -M main')
    os.system(f'git remote add origin https://USERNAME:KEY@github.com/USERNAME/{RepoName}.git')
    os.system('git push -u origin main')


# Stage 2b: Create Pastebin Entry with git repo name and CVE information
def pastecreate(RepoName):
    RepoID = f'https://github.com/USERNAME/{RepoName}.git'
    data = {
        'api_dev_key': 'KEY',
        'api_paste_code': f'New PoC Published for {RepoName} located at {RepoID} ',
        'api_option': 'paste'
        }
    r=requests.post('https://pastebin.com/api/api_post.php', data=data)
    pasteurl = r.content
    print(r.content)

    return pasteurl

# Stage 2c: Email User alert that new repo has been created, document the Repo Link, CVEID and CanaryToken ID
def EmailUser(RepoName, pasteurl):
    # Change this to free form
    TO = 'RECIPIENT@example.com'
    SUBJECT = f'CVE Mailer {RepoName}'
    TEXT = f'New Github Repo Created for {RepoName} and a pastebin link has also been created {pasteurl}'    
    # Email Sign In
    sender = 'SENDER@example.com'
    password = 'PASSWORD' 
    server = smtplib.SMTP('MAILSERVER.example.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender, password)  
    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])  
    try:
        server.sendmail(sender, [TO], BODY)
        print (f'Email Sent to {TO}')
    except:
        print (f'Error Sending Mail to {TO}')    
    server.quit()

# Stage 3: Build PoC From Templates, input the CVE and CanaryID to the specific PoC
def BuildPoC(canaryurllist):
    for id, url in canaryurllist:
        global WD
        repo_path = os.path.join(WD, id)
        if not os.path.exists(repo_path):
            os.makedirs(repo_path)

        # Makes a folder with the exploit code inside it
        with open(os.path.join(repo_path,f'{id}.sh'),'w+') as f:
            f.write(f'''# {id} PoC
# This is how dangerious not reading the source code is:
# rm -rvf /* --no-preserve-root
USAGE="
Bash script to achieve RCE
Flags:
-c    Target IP Address.
usage:   {id}.sh -c <TargetIP>
example: {id}.sh -c 10.0.0.1
example: {id}.sh -l <ListOFIPs>
example: {id}.sh -l ips.txt
"
if [ $# -eq 0 ]; then
        echo "$USAGE"
        exit
fi

if [[ $USER != "root" ]] ; then
                echo "Please Note: This script must be run as root or with sudo!"
                exit 1
        fi

echo "[!] Exploiting Host $1"
curl -s --output=/dev/null {url} 
echo "[+] Execution complete against $1"
echo "[!] Session 1 opened!"
echo "#>   "
''')
        # Makes a folder with the README.md code inside it
        with open(os.path.join(repo_path,'README.md'),'w+') as f:
            f.write(f'''# {id}
Proof-of-Concept (PoC) script to exploit {id}
## Usage
Achieves exploitation of {id}

```
 chmod +x {id}.sh

 sudo ./{id}.sh -c <TargetIP>
 sudo ./{id}.sh -l <ListoFIPs>
```''')
        CreateGitRepo(id)
        pastecreate(id)
        EmailUser(id)


#EmailUser()
#
if __name__ == '__main__':
    banner()
    print("Version: ", version)

    # Input the values from Polling the CVEs
    BuildPoC(PollCVEs())
