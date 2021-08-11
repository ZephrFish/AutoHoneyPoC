# AutoHoneyPoC
AutoPoC Generator HoneyPoC ULTIMATE EDITION

## Usage:
`python3 autopoc.py`

## Example Output
```
CVE-2021-23388
5.0
CVE-2020-1920
5.0
CVE-2021-24316
4.3
3/5
[*] Making Directory CVE-2021-23388
[*] Openning and processing Data in /path/to/template/template.poc.sh ...
[*] Closing /path/to/template/template.poc.sh ...
[*] CVE-2021-23388.sh generated!
[*] Openning and processing Data in /path/to/template/template.poc.go ...
[*] Closing /path/to/template/template.poc.go ...
[*] CVE-2021-23388.go generated!
[*] Cross Compile Success!
[*] Openning and processing Data in /path/to/template/template.poc.readme.md ...
[*] Closing /path/to/template/template.poc.readme.md ...
[*] README.md generated!
b'https://pastebin.com/example'
Initialized empty Git repository in /path/to/template/CVE-2021-23388/.git/
[master (root-commit) b7115c3] CVE-2021-23388 Commit
 3 files changed, 55 insertions(+)
 create mode 100644 CVE-2021-23388.exe
 create mode 100644 CVE-2021-23388.sh
 create mode 100644 README.md
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 16 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 3.37 MiB | 5.07 MiB/s, done.
Total 5 (delta 0), reused 0 (delta 0)
To https://github.com/example/CVE-2021-23388.git
 + b96f2b3...b7115c3 main -> main (forced update)
```

## Requirements in terms of Creds (.creds.env):
- CVE_SEARCH : The search term for type of CVE to search for and generate
- CANARY_AUTH_TOKEN : CanaryTokens API Key
- CANARY_API_URL : Unique canary API url blah.canary.tools
- GITHUB_USERNAME : Username of git account to upload to
- GITHUB_TOKEN : Personal access token for user
- PASTE_API_KEY : API token for pastebin
- EMAIL_TO : Email to send the output to and from
- EMAIL_PASSWORD : Password for auth
- EMAIL_SERVER :  Server URL
- EMAIL_SERVER_PORT : Server port

###  What This Script Does:
1. Stage 1: Poll CVEs from Database URL and then drop them into a list to itterate through and create canary tokens for each CVE
2. Stage 2a: Create Git Repo and Push updates to Repo
3. Stage 2b: Email User alert that new repo has been created, document the Repo Link, CVEID and CanaryToken ID
4. Stage 2c: Create Pastebin Entry with git repo name and CVE information
5. Stage 3: Build PoC From Templates, input the CVE and CanaryID to the specific PoC

## Locations for Stuff

- Canary Token: https://EXAMPLE.canary.tools/nest/
- Github: https://github.com/USER/CVE-X.git
- Pastebin: https://pastebin.com/randomstring

## Thanks
- https://twitter.com/BufferOfStyx - Helped with modularization
- https://twitter.com/GossiTheDog - Initial funding of DO VPS for fuckery
- https://twitter.com/0x616e6874 - Helped with streamlining code

### TODO Pipeline
#### Argparse - Got int working, need to factor in CVE search and debug/verbose mode.
-  -a : int for amount of CVEs
-  -d : debug, set default to false 
-  -s : Specific phrase search in ares CVE_Search lib - to read
-  -v : Turn on verbose output

#### More Functions
- Slack notifier - technically implemented via canary tokens
- Discord notifier
- Start to build dashboard of accounts destroyed on git and work out where/when created/deleted

# Talk Ideas
- When in Doubt: Fuck Around Get Found Out
- Disinformation As A Service: F Around, Get Found Out

## Information + data 
- Gathering where the CVE details get dropped
- Gather data around executions and mapping


# What the Binary / Payload does
- TODO: Adding to the Joke aspect and profile

