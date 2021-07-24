# Compile go Function
from src.functions.compileGo import compile_go
# Get Path of CVE Folder
from src.functions.getCvePath import getCvePath

#Functions for editing template
from src.template_edit_functions.replaceInformation import replaceInformation
from src.template_edit_functions.open_close_write_Template import open_template, close_template, write_template

def create_payload(cve, canaryUrl, extension, PWD, target_string_cve, target_string_canaryUrl, template_directory):
	#Concatinating the default_template root name, and the template extesnion. So we get our desired target file template
	#Example : template.poc + .sh = template.poc.sh
	path = getCvePath(PWD, cve)

	file = template_directory + extension

	#Getting data from the target template 
	data = open_template(file)

	#Replacing the information in the template
	data = replaceInformation(data, cve , canaryUrl, target_string_cve, target_string_canaryUrl)

	#Writing the change template to a cve file
	write_template(path, data, cve, extension)
	if extension == ".go":
		compile_go(path, cve)
