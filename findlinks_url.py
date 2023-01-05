import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
#set the URL to get links from below
url = 'https://kb.joshtheadmin.com'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

for link in soup.find_all('a'):
	domain = urlparse(link.get('href')).netloc
	# print the full link if it is a bit.ly link, use case had bit.ly links but it would be a good idea to add checks for other URL shortners
	# in the use case, I was looking to whitelist links on a webpage, and I did not want to whitelist the domain for a URL shortener
	if "bit.ly" in domain:
		print(f"{urlparse(link.get('href')).netloc}{urlparse(link.get('href')).path}")
	elif domain.isspace() or (domain == ""):
		continue
	else:
		print(domain)
