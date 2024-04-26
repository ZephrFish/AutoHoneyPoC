"""
# Generic Function
+ Open Template
~ Description : the function will open the file given, and return the data inside the file
~ @file	: name of file to open
~ return data : returns the template in data format to be edited later.
"""


def open_template(file):
    template = open(file, "rt")
    data = template.read()
    print(f"[*] Openning and processing Data in {file} ...")
    close_template(template, file)
    return data


"""
# Generic Function
+ Close Template
~ Description : closes the template, to avoid errors occuring, not neccesary but important to do just in case.
~ @template   : template variable that was returned from open_template
~ @file	: name of the file to close, the same as the open_template file name.
"""


def close_template(template, file):
    template.close()
    print(f"[*] Closing {file} ...")


"""
# Generic Function
+ Write Template
~ Description : Writes the data from a template to a new file inside of the CVE Folder
~ @extension  : this is the same as template in the above thing but change the variable name because we will be using it as a file extension
~ @cve		  : cve is a string of the CVE to write as the file names
~ @path		  : path to place we are supposed to write to
~ @data		  : data we are supposed to write to
"""


def write_template(path, data, cve, extension):
    file = cve + extension
    filewithpath = path + file
    output = open(filewithpath, "w+")
    output.write(data)
    output.close()
    print(f"[*] {file} generated! ")
