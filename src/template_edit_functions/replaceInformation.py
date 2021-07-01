'''
# Important Function
+ replaceInformation
~ Description : this function will check the template we are interacting with and then replace the information that is important
~ @data       : data that is from the template to be edited
~ @cve        : cve string to replace the target string : Example CVE-2020-1337
~ @canaryUrl  : canaryUrl string to replace the target string
~ @target_string_cve : target string we are searching for to replace with the CVE
~ @target_string_canaryURL : target string we are searching for to replace with the Canary URL
~ return data : returns the now edited data
'''
def replaceInformation(data, cve , canaryUrl, target_string_cve, target_string_canaryUrl):
	data = data.replace(target_string_cve, cve)
	data = data.replace(target_string_canaryUrl, canaryUrl)
	return data
