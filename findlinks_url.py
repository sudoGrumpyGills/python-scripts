#script to pull links from a webpage, and print a list of the unique domains, this is for whitelisting requests
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
#set the URL to get links from below
url = 'https://www.assaabloydooraccessories.us/en/resource-library/catalogs-brochures/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
url_list = []
for link in soup.find_all('a'):
	domain = urlparse(link.get('href')).netloc
	#my use case had bit.ly shortened links, I needed the full links for these because I can't whitelist bit.ly entirely
	if "bit.ly" in domain:
		url_list.append(f"{urlparse(link.get('href')).netloc}{urlparse(link.get('href')).path}")
	elif domain.isspace() or (domain == ""):
		continue
	else:
		url_list.append(domain)
for domain in set(url_list):
	print (domain)
