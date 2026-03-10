import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

name_regex = re.compile(r"known_by_([A-Za-z]+)\.html")
namelist = []

for tag in soup.find_all('a'):
    href = tag.get('href')
    if not href:
        continue
    print(href)  # show every link (optional)

    m = name_regex.search(href)
    if m:
        namelist.append(m.group(1))
        if len(namelist) >= 4:   # stop after 4 names
            break

print("Names found:", namelist)
