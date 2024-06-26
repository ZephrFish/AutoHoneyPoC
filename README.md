# AutoHoneyPoC
AutoPoC Generator HoneyPoC ultimate edition.

If this is the first time you've heard of or seen the project, you'll want to read the blog post. https://blog.zsec.uk/honeypoc-ultimate/

![image](https://user-images.githubusercontent.com/5783068/191644772-d45817d5-00ff-49af-b874-38d09055a72b.png)


**While I'm releasing AutoPoC, the framework on its own is harmless as it requires some pre-requisites to build the automated backend, but the outputted code is technically malware, so be careful what you do with it, and it's for educational purposes etc; I'm not liable if you use it for crime or other chaos.**

All accounts in the commit history where you might see creds have either been flagged by GitHub as malicious or flattened ;).

Sister Project: [SandboxSpy](https://github.com/ZephrFish/SandboxSpy)

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
1. Stage 1: Poll CVEs from the Database URL and then drop them into a list to iterate through and create canary tokens for each CVE
2. Stage 2a: Create Git Repo and Push updates to Repo
3. Stage 2b: Email User alert that new repo has been created, document the Repo Link, CVEID and CanaryToken ID
4. Stage 2c: Create a Pastebin Entry with the git repo name and CVE information
5. Stage 3: Build PoC From Templates, input the CVE and CanaryID to the specific PoC

## Locations for Stuff

- Canary Token: https://EXAMPLE.canary.tools/nest/
- Github: https://github.com/USER/CVE-X.git
- Pastebin: https://pastebin.com/randomstring

## Thanks
- https://twitter.com/BufferOfStyx - Helped with modularization of some of the code, also helped with initial brainstorming ideas


#### More Functions
- Slack notifier - technically implemented via canary tokens, but a webhook URL/method is a WIP
- Discord notifier
- Start to build a dashboard of accounts destroyed on git and work out where/when created/deleted

## Information + data 
- Gathering where the CVE details get dropped
- Gather data around executions and mapping


## Detection and Response
I'm not a blue teamer or detection engineer by trade; however, the Yara rules before are my attempt at some detection for the domains and binaries being executed historically within your environment.

```
rule HoneyPoC_URLDetect {

meta:
description = "HoneyPoC AutoPoC URL detection"
author = "Andy Gill"
reference = "blog.zsec.uk/honeypoc-ultimate/"
date = "2021/11/13"
hash = "b6807027ac171252cf47eb28454c044644352c9f2fabd65d3f23075a0e395768"

strings:
 $a = "honeypoc.io" nocase
 $b = "canarytokens.com" nocase
 $c = "givemeyourpasswords.ninja" nocase
 
 condition:
    $a or $b or $c
 }
```
The following yara rule can be used with something like PasteHunter to search for specific strings in Pastebin links.

```
rule HoneyPoC_Pastebin
{
    meta:
    description = "HoneyPoC AutoPoC Pastebin detection"
    author = "Andy Gill"
    reference = "blog.zsec.uk/honeypoc-ultimate/"
    date = "2021/11/13"

    strings:
        $a = "New PoC Published for" nocase wide ascii fullword


    condition:
        $a
}
```
