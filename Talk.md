# Planning Talk
- Title
- Layout
- What I want to cover

# Fuck Around & Get Found Out: Disinformation As A Service
## Abstract
CVEs and big vulnerabilities are being released on a daily basis with and without proofs of concept. 14th July 2020 was a day that rocked the internet, it was the day HoneyPoC was born. What started as a joke proof of concept quickly built traction and built a new class of disinformation campaigns. 

This talk will dive into not only how HoneyPoC came to be but will also explain how I took it one step further in exploring disinformation as a service and exploring the scientific method of f*ck around find out. I will also be demoing how I took a simple piece of proof of concept code and build a DaaS campaign out of it which poisoned many CTI feeds, found its way into some interesting situations. Uncovered APTs, Insider threats and charlatans alike. 

Not all talks are Red/Blue/Purple, some are learning opportunities for all. HoneyPoC opened the eyes of many folks and why is it important to be careful about the Proof Of Concepts(POC) that you download/review. What started off as a minor troll turned into an integrated research project, the talk will embark on knowledge about threat intelligence and educate the watchers. Who watches the watchpeople?

This was a particularly "amusing" troll because the sort of people who keep up with CVEs and look for proof-of-concept exploits should really know better than to run random code they just got off GitHub without checking what it does.

# Layout
## Introduction to HoneyPoC
### How it came to be
### Some stats on initial 1,2 & 3.0

## Lasting Impact
### CTI Feeds
### Distrust in raw PoCs

## Disinformation As A Service aka Automating HoneyPoC
### Introducing AutoPoC
####  What This Script Does:
1. Stage 1: Poll CVEs from Database URL and then drop them into a list to itterate through and create canary tokens for each CVE
2. Stage 2a: Create Git Repo and Push updates to Repo
3. Stage 2b: Email User alert that new repo has been created, document the Repo Link, CVEID and CanaryToken ID
4. Stage 2c: Create Pastebin Entry with git repo name and CVE information
5. Stage 3: Build PoC From Templates, input the CVE and CanaryID to the specific PoC

### Explaining structure - how it works

## Stats from X months and information learned

### The Data breakdown 
- Total POCS Generated
- Total Amount of Github Accounts
- Total runs
- Breakdown by CVE
- Breakdown by Geolocation
- Interesting locations

## Lessons Learned
### Future Plans
### Threat Actors
#### TTPs Generated
#### Detecting AutoPoC
### SandBoxSpy & Stage 0 implants

## Conclusion
