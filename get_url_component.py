import re

url_dict = {}
delimiter = ['/', '?', '.', '=', '-', '_']

def get_url_component(url):
	protocol = ''
	domain = ''
	path = ''
	component = []
	link = ''

	if url.find("//") != -1:
		# Find position of // in URL
		double_slashes_pos = url.index('//') 				
		# Get protocol in URL
		protocol = url[:(double_slashes_pos-1)]				
		link = url[(double_slashes_pos+2):]					
	else :
		link = url

	# Split domain & path	
	link_component = link.split('/',1) 					
	domain = link_component[0]
	path = link_component[1]

	# Add URL into URL_dict
	if url not in url_dict.keys():						
		url_dict[url] = {"Protocol" : protocol, "Domain" : domain, "Path" : path}
	return url_dict[url]	

def get_URL_token(url_component):
	token = re.split(r'\W+',url_component)
	return token

# Count Domain or Path Token
def token_count(url_component):								
	token =  re.split(r'\W+',url_component)
	return len(token)

def avg_token_length(url_component):
	# Remove special char
	token_length = re.sub(r'\W+','',url_component)			
	return float(len(token_length) / token_count(url_component))

def longest_length(url_component):
	token =  re.split(r'\W+',url_component)
	longest_token = token[0]					

	for i in range(len(token)-1):
		if len(token[i]) < len(token[i+1]):
			longest_token = token[i+1]

	return {'Longest_token': longest_token, 'Longest_token_length': len(longest_token)}

def dot_count(url):
	return url.count('.')

def slash_count(url):
	return url.count('/')

def a_symbol(url):
	if url.count('@') == 0:		
		# False means url do not have @ symbol							
		return False											
	# True means url have @ symbol	
	return True													

def malicious_special_char(url):
	malicious_special_char_list =  ['!',',','#','$','^','*','(',')','+','{','}']
	for i in range(len(malicious_special_char_list)):
		if url.count(malicious_special_char_list[i]) != 0:
			# True means url have malicious special character
			return True				
	# False means url do not have malicious special character									
	return False														



if __name__ == "__main__":
	url = 'http://google.com.vn/abc/abc.php'
	#url2 = 'https://facebook.com.vn/dsd.asp'	
	get_url_component(url)
	#get_url_component(url2)
	print(url_dict)
	