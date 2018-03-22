import requests
import json
import dns.resolver
from pprint import pprint
apikey = '1d471549db57f7232ad1d53e0752167cadb854becd72a44566ba57e0f1886350'

def getResolvedIPCount(domain):
	url = 'https://www.virustotal.com/vtapi/v2/domain/report'
	params = {'apikey': apikey, 'domain': domain}
	response = requests.get(url, params=params)
	return len(response.json()['resolutions'])

# def getNameServerCount(domain):
# 	return len(dns.resolver.query(domain,'ns'))
def getNameServerCount(domain):
	url = 'https://www.virustotal.com/vtapi/v2/domain/report'
	params = {'apikey': apikey, 'domain': domain}
	response = requests.get(url, params=params)
	return (response.json()['whois'].count('Name Server'))/2