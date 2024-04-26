import os


def create_directory(cve):
    print(f"[*] Making Directory {cve}")
    os.system(f"mkdir {cve}")
