import codecs
import csv
from pathlib import Path

def get_path():
	"""
	A function to get the current path to bot.py
	Returns:
	 - cwd (string) : Path to bot.py directory
	"""
	cwd = Path(__file__).parent.parent.parent
	#cwd = Path(__file__).resolve().parent
	cwd = str(cwd)
	return cwd

def read_csv(filename):
	"""
	A function to read a json file and return the data.
	Params:
	 - filename (string) : The name of the file to open
	Returns:
	 - data (dict) : A dict of the data in the file
	"""
	to_return = []
	cwd = get_path()
	with open(cwd+'/data/'+filename+'.csv', 'r') as file:
		data = list(csv.reader((line.replace('\0','' ) for line in file), delimiter=','))
		return data

def write_csv(data, fieldnames, filename):
	"""
	A function used to write data to a json file
	Params:
	 - data (dict) : The data to write to the file
	 - filename (string) : The name of the file to write to
	"""
	cwd = get_path()
	with open(cwd+'/data/'+filename+'.csv', 'w') as file:
		writer = csv.DictWriter(file, fieldnames=fieldnames)
		writer.writeheader()
		for da in data:
			writer.writerow(da)

def append_csv(data, fieldnames, filename):
    """
    A function used to write data to a json file
    Params: 
     - data (dict) : The data to write to the file
     - filename (string) : The name of the file to write to
    """
    cwd = get_path()
    with open(cwd+'/data/'+filename+'.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        for da in data:
            writer.writerow(da)
