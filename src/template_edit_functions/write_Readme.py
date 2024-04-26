"""
# Generic Function
+ Write Readme
~ Description : Write the readme information to the README.md file of that directory
~ @cve		: cve is a string of the CVE to write as the file names
~ @path	   : path to place we are supposed to write to
~ @data	   : data we are supposed to write to
"""


def write_readme(path, data, cve):
    file = "README.md"
    filewithpath = path + file
    output = open(filewithpath, "w+")
    output.write(data)
    output.close()
    print(f"[*] {file} generated! ")
