# To run this, download the BeautifulSpup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import ssl
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = inpur('Enter -')
html = urllib.request.urlopen(url, contxt=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
