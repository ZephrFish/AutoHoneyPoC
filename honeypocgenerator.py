#!/usr/bin/env python3

# Imports for various functions within src, additional libs are imported per function
import json
import hashlib
import argparse
import sys
import random
import string
import os
import smtplib
import time
import re
import ipaddress
from ares import CVESearch
import requests
import requests_cache
from collections import namedtuple

# Functions
from src.functions.getCVEs import PollCVEs
from src.functions.getHashSha256 import getHash
from src.functions.compileGo import compile_go
from src.functions.getCvePath import getCvePath

# Create functions
from src.create_functions.create_readme import create_readme
from src.create_functions.create_directory import create_directory
from src.create_functions.create_payload import create_payload

# Upload functions
from src.upload_functions.createPaste import createPaste
from src.upload_functions.createGitRepo import createGitRepo
from src.upload_functions.emailUser import emailUser

# File format helpers
from src.utils.json_helper import read_json
from src.utils import cve_helper

# Template and README functions
from src.template_edit_functions.replaceInformation import replaceInformation
from src.template_edit_functions.open_close_write_Template import open_template, close_template, write_template
from src.template_edit_functions.write_Readme import write_readme

'''
# Global Variables
~ Description : These are here because they sit better here then anywhere else in the code multiple places use them,
				and having them here makes them easily editable.

@ default_template			: this is what the template root name is so for example "template.poc", then we add the extension for each payload to generate.
@ target_string_cve			: the string to search for in the template to then replace to be the CVE information
@ target_string_canaryUrl	: the string to search for in the template to then replace to be the Canary Urls
@ PWD						: working directory that the python3 program was executed from
@ amount					: amount of cve's to requests
'''
global amount
global debugging
global default_template
global template_extensions
global target_string_cve
global target_string_canaryUrl
global PWD

cvss = 1
amount = "5"
# Does not work at the moment
debugging = True

PWD = os.path.dirname(os.path.realpath(__file__))

template_extensions = ['.sh','.go']
default_template_directory = "/templates"
default_template = "template.poc"
target_string_cve = "$cve"
target_string_canaryUrl = "$canary_url"

#Path to the default template, only need to append extension later to select each template
template_directory = PWD + default_template_directory + "/" + default_template


# Builds Requests Cache with DB called TrollList - Does Monkey Patching of requests
requests_cache.install_cache(os.path.join(PWD, "TrollList"), expire_after=3600)

global CANARY_AUTH_TOKEN
global CANARY_API_URL
global GITHUB_USERNAME
global GITHUB_TOKEN
global PASTE_API_KEY
global EMAIL_TO
global EMAIL_PASSWORD
global EMAIL_SERVER
global EMAIL_SERVER_PORT
global CVE_SEARCH

data = read_json(".creds")

CVE_SEARCH = data ['CVE_SEARCH']

CANARY_AUTH_TOKEN = data['CANARY_AUTH_TOKEN']
CANARY_API_URL = data['CANARY_API_URL']

GITHUB_USERNAME = data['GITHUB_USERNAME']
GITHUB_TOKEN = data['GITHUB_TOKEN']

PASTE_API_KEY = data['PASTE_API_KEY']

EMAIL_TO = data['EMAIL_TO']
EMAIL_PASSWORD = data['EMAIL_PASSWORD']
EMAIL_SERVER = 	data['EMAIL_SERVER']
EMAIL_SERVER_PORT = data['EMAIL_SERVER_PORT']

def do_more_shit(cve):
	createPaste(cve[0], GITHUB_USERNAME, PASTE_API_KEY)
	createGitRepo(cve[0], cve[2], GITHUB_USERNAME, GITHUB_TOKEN, PWD)
	# Comment out when we don't want a notification email
	#emailUser(cve[0], EMAIL_TO, EMAIL_PASSWORD, EMAIL_SERVER, EMAIL_SERVER_PORT)

def generatePoc(cve):
	create_directory(cve[0])
	for template in template_extensions:
		create_payload(cve[0], cve[1], template, PWD, target_string_cve, target_string_canaryUrl, template_directory)
	create_readme(template_directory, cve[0], cve[2], PWD, target_string_cve)
	do_more_shit(cve)

def main():

	cveList = PollCVEs(CANARY_AUTH_TOKEN, CANARY_API_URL, amount, cvss)

	count = 0
	for cve in cveList:
		generatePoc(cve)
		print("\r")
	print("[*] Making sure you didn't fuck up the cve and that canary shit")

	print("[*] Initialising and Sorting Shit out()")

	print("[*] Removing files...")

if __name__ == "__main__":
	main()

