# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# or pip install beautifulsoup4 to ensure you have the latest version
# and unzip it in the same directory as this file
# http://py4e-data.dr-chuck.net/known_by_Fikret.html

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl # defauts to certicate verification and most secure protocol (now TLS)
# import re

# # Ignore SSL/TLS certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input("URL: ")
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
# namelist = list()


# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     href = tag.get('href', None)
#     text = tag.get_text(strip=True)
#     print(href)
#     names = re.findall("known_by_([A-Za-z]+)\\.html", href)
#     if names:
#         for name in names:
#             namelist.append(name)
#             if len(namelist) >= 4:
#                 break
#     if len(namelist) >= 4:
#         break
# print(namelist)


# working

import urllib.request
from bs4 import BeautifulSoup

# Starting URL
url = 'http://py4e-data.dr-chuck.net/known_by_Tailee.html'

# Repeat 4 times
for i in range(7):
    # Open the URL and read the HTML
    html = urllib.request.urlopen(url).read()
    
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all <a> (link) tags
    links = soup('a')
    
    # Pick the link at position 3 (index 2 in Python)
    link = links[17]
    print(link)
    
    # Get the new URL from the href attribute
    url = link.get('href')
    
    # Print the name (text of the link)
    print(link.text)

# Print the final name again
print("Last name in sequence:", link.text)
