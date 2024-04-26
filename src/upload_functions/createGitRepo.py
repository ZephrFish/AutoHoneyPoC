import os

import requests

"""
# Generic Function
+ CreateGitRepo
~ Description : Creates Github repo, by fucking doing some shit, os.system commands, careful of unsanatized input !security
"""


def createGitRepo(cve, summary, GITHUB_USERNAME, GITHUB_TOKEN, PWD):
    # Create Repo and Init it
    os.chdir(os.path.join(PWD, cve))
    os.system("git init")
    os.system("git add README.md")
    os.system(f"git add {cve}.sh")
    os.system(f"git add {cve}.exe")
    data = {"name": cve, "description": f"PoC for exploiting {cve} : {summary}"}
    r = requests.post(
        "https://api.github.com/user/repos",
        json=data,
        auth=(GITHUB_USERNAME, GITHUB_TOKEN),
    )
    os.system('git config user.name "User"')
    os.system('git config user.email "User@example.com"')
    os.system(f'git commit -m "{cve} Commit"')
    os.system("git branch -m main")
    os.system(
        f"git remote add origin https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{cve}.git"
    )
    os.system("git push -u origin main --force")
    os.chdir(PWD)
