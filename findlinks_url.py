import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
#set the URL to get links from below
url = 'https://kb.joshtheadmin.com'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

for link in soup.find_all('a'):
	domain = urlparse(link.get('href')).netloc
	if "bit.ly" in domain:
		print(f"{urlparse(link.get('href')).netloc},{urlparse(link.get('href')).path}")
	elif domain.isspace() or (domain == ""):
		continue
	else:
		print(domain)