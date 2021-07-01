import json
import requests

# Stage 2b: Create Pastebin Entry with git repo name and CVE information
def createPaste(cve, GITHUB_USERNAME, PASTE_API_KEY):
	RepoID = f'https://github.com/{GITHUB_USERNAME}/{cve}.git'
	data = {
		'api_dev_key': PASTE_API_KEY,
		'api_paste_code': f'New PoC Published for {cve} located at {RepoID} ',
		'api_option': 'paste'
		}
	r=requests.post('https://pastebin.com/api/api_post.php', data=data)
	print(r.content)
