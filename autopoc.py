#!/usr/bin/env python3
# AutoPoC baseline script
# ZephrFish 2022 update

# Imports for various functions within src, additional libs are imported per function
# Version 2.0 - Adding in arguments
import argparse
import os

import requests_cache

from src.create_functions.create_directory import create_directory
from src.create_functions.create_payload import create_payload

# Create functions
from src.create_functions.create_readme import create_readme

# Functions
from src.functions.getCVEs import PollCVEs
from src.upload_functions.createGitRepo import createGitRepo

# Upload functions
from src.upload_functions.createPaste import createPaste

# File format helpers
from src.utils.json_helper import read_json

# Template and README functions


# Colours
# Not all of these will get used but I like this block of code I borrowed from some stack overflow thread
def prRed(skk):
    print("\033[91m {}\033[00m".format(skk))


def prGreen(skk):
    print("\033[92m {}\033[00m".format(skk))


def prYellow(skk):
    print("\033[93m {}\033[00m".format(skk))


def prLightPurple(skk):
    print("\033[94m {}\033[00m".format(skk))


def prPurple(skk):
    print("\033[95m {}\033[00m".format(skk))


def prCyan(skk):
    print("\033[96m {}\033[00m".format(skk))


def prLightGray(skk):
    print("\033[97m {}\033[00m".format(skk))


def prBlack(skk):
    print("\033[98m {}\033[00m".format(skk))


"""
# Global Variables
~ Description : These are here because they sit better here then anywhere else in the code multiple places use them,
				and having them here makes them easily editable.

@ default_template			: this is what the template root name is so for example "template.poc", then we add the extension for each payload to generate.
@ target_string_cve			: the string to search for in the template to then replace to be the CVE information
@ target_string_canaryUrl	: the string to search for in the template to then replace to be the Canary Urls
@ PWD						: working directory that the python3 program was executed from
@ amount					: amount of cve's to requests
"""
global amount
global debugging
global default_template
global template_extensions
global target_string_cve
global target_string_canaryUrl
global PWD

# Arguments
"""
# Argument Parsing
~ Description : The functions below are used for argument parsing
Args:
-a : int for amount of CVEs
-d : debug, set default to false
-s : Specific phrase search in ares CVE_Search lib - to read
-v : Turn on verbose output
"""

parser = argparse.ArgumentParser(
    description="AutoPoC Tooling", prog="autopoc.py", usage="%(prog)s [options]"
)

# Arguments
parser.add_argument(
    "-a",
    action="store",
    dest="CVEAmount",
    default="5",
    help="Number of CVEs to request, defaults to 5",
)
# parser.add_argument('-d', action='store', dest='DebugMode', default=None, help='turn on debug')
# parser.add_argument('-s', action='store', dest='CVESearch', default=None, help='Specific phrase search in ares CVE_Search lib')
# parser.add_argument('-v', action='store', dest='Verbose', default=None, help='turn on verbose mode')

args = parser.parse_args()

cvss = 1
amount = args.CVEAmount
# Does not work at the moment
# debugging = True

PWD = os.path.dirname(os.path.realpath(__file__))

template_extensions = [".sh", ".go"]
default_template_directory = "/templates"
default_template = "template.poc"
target_string_cve = "$cve"
target_string_canaryUrl = "$canary_url"

# Path to the default template, only need to append extension later to select each template
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

CVE_SEARCH = data["CVE_SEARCH"]

CANARY_AUTH_TOKEN = data["CANARY_AUTH_TOKEN"]
CANARY_API_URL = data["CANARY_API_URL"]

GITHUB_USERNAME = data["GITHUB_USERNAME"]
GITHUB_TOKEN = data["GITHUB_TOKEN"]

PASTE_API_KEY = data["PASTE_API_KEY"]

EMAIL_TO = data["EMAIL_TO"]
EMAIL_PASSWORD = data["EMAIL_PASSWORD"]
EMAIL_SERVER = data["EMAIL_SERVER"]
EMAIL_SERVER_PORT = data["EMAIL_SERVER_PORT"]


def do_more_shit(cve):
    createPaste(cve[0], GITHUB_USERNAME, PASTE_API_KEY)
    createGitRepo(cve[0], cve[2], GITHUB_USERNAME, GITHUB_TOKEN, PWD)
    # Comment out when we don't want a notification email
    # emailUser(cve[0], EMAIL_TO, EMAIL_PASSWORD, EMAIL_SERVER, EMAIL_SERVER_PORT)


def generatePoc(cve):
    create_directory(cve[0])
    for template in template_extensions:
        create_payload(
            cve[0],
            cve[1],
            template,
            PWD,
            target_string_cve,
            target_string_canaryUrl,
            template_directory,
        )
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
