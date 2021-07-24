from src.functions.getHashSha256 import getHash
from src.functions.getCvePath import getCvePath
from src.template_edit_functions.open_close_write_Template import open_template
from src.template_edit_functions.write_Readme import write_readme

def create_readme(template_directory, cve, summary, PWD, target_string_cve):
	extension = ".readme.md"
	file = template_directory + extension

	data = open_template(file)

	path = getCvePath(PWD, cve)

	go_hash = getHash(path + cve + ".exe")

	data = data.replace("$sha256hash", go_hash)
	data = data.replace(target_string_cve, cve)
	data = data.replace("$summary", summary)

	write_readme(path, data, cve)
