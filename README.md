# AutoHoneyPoC
AutoPoC Generator HoneyPoC ULTIMATE EDITION

## Usage:
`python3 autopoc.py`

###  What This Script Does:
1. Stage 1: Poll CVEs from Database URL and then drop them into a list to itterate through and create canary tokens for each CVE
2. Stage 2a: Create Git Repo and Push updates to Repo
3. Stage 2b: Email User alert that new repo has been created, document the Repo Link, CVEID and CanaryToken ID
4. Stage 2c: Create Pastebin Entry with git repo name and CVE information
5. Stage 3: Build PoC From Templates, input the CVE and CanaryID to the specific PoC
