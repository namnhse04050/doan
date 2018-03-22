import get_url_component as lexical
import virustotal_api as host_base

url = 'uluulupetcafe.sg/pony/panelnew/admin.php'
domain = ''
path = ''
domain = lexical.get_url_component(url)["Domain"]
path = lexical.get_url_component(url)['Path']
print('Domain: ',domain)
print('Path: ',path)

print('Domain token count: ', lexical.token_count(domain))
print('Path token count: ', lexical.token_count(path))
print('Avg domain token length: ',lexical.avg_token_length(domain))
print('Avg path token length: ',lexical.avg_token_length(path))
print('Longest domain token: ', lexical.longest_length(domain))
print('Longest path token: ', lexical.longest_length(path))
print('Number of dot: ', lexical.dot_count(url))
print('Number of slash: ', lexical.slash_count(url))
print('@ symbol: ', lexical.a_symbol(url))
print('Malicious special char: ', lexical.malicious_special_char(url))
print('Number of resolved IP: ', host_base.getResolvedIPCount(domain))
print('Number of name server: ', host_base.getNameServerCount(domain))