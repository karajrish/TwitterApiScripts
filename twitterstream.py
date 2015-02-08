import json
import requests
from requests_oauthlib import OAuth1

api_key = ""
api_secret = ""
access_token_key = ""
access_token_secret = ""


url = 'https://stream.twitter.com/1/statuses/sample.json'
auth = OAuth1(api_key, api_secret, access_token_key, access_token_secret)

r = requests.get(url, auth=auth, stream=True, timeout=5)
cnt=10
# print type(r)
for line in r.iter_lines():

	if cnt==0:
		break
	if line:
		#print "printing"
		j=json.loads(line)
		if 'delete' in j.keys():
			# print "bypassing delete"
			continue
		else:
			if j['lang'] !='en':
				continue
			# elif '#manu' not in j['text'].lower():
			# 	continue
			else:
				print type(line)
				print type(r.iter_lines)
				#print j.keys()
				print j['created_at'], " ", j['place'], j['geo']
				print j['text']
				cnt=cnt-1
				print "\n"
		# print "\n"
		# print j['lang']
		# cnt=cnt-1	
   		# print json.loads(line)
   		
