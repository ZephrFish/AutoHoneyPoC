from collections import namedtuple

import requests
from ares import CVESearch


def PollCVEs(CANARY_AUTH_TOKEN, CANARY_API_URL, amount, cvss):
	cveSer = CVESearch()
	# Grab last CVE number
	CVEList = cveSer.last(amount)


	# Print out Last output
	# print([Entry['id'] for Entry in CVEList][-1])
	# Return list of values in array
	#print(str([Entry['id']) + '\r' + str(Entry['summary']) + '\r' +  str(Entry['cvss']) for Entry in CVEList])

#	for Entry in CVEList:
#		print("" + Entry['id'])
#		print("" + Entry['summary'])
#		print("" + str(Entry['cvss']))
#		print('\r')


	# Iterate through the strings in the array

	canaryurllist = []
	# Creates a name space of the pair of canary url and CVE id
	CVECanaryPair = namedtuple('CVECanaryPair', ['id', 'url', 'summary', 'cvss'])
	count = 0
	for CVEID in CVEList:
		data = {
			'auth_token': CANARY_AUTH_TOKEN,
			'memo': CVEID['id'],
			'kind': 'http'
			}
		response = requests.post(CANARY_API_URL, data=data)
		canaryurl = response.json()['canarytoken']['url']
		#pair = CVECanaryPair(id=CVEID['id'],url=canaryurl)

		if CVEID['cvss'] == None and cvss != 0:
			continue
		elif (int(CVEID['cvss']) >= int(cvss)):
			print(CVEID['id'])
			print(CVEID['cvss'])
			pair = CVECanaryPair(id=CVEID['id'], url=canaryurl, summary=CVEID['summary'], cvss=CVEID['cvss'])
			canaryurllist.append(pair)
			count += 1
		else:
			continue

	print(f'{count}/{amount}')
	return canaryurllist
