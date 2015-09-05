import re
import urllib
from BeautifulSoup import *


# open the "nld_urls.txt" in the reading mode
urlhand = open('nld_urls.txt', 'r')
data = urlhand.read()
lst = data.rsplit(',')

# remove empty elements
while lst.count("") > 0:
    lst.remove("")

rawhand = open('nld_rawtext.txt', 'w')

for url in lst:
    url = str(url.strip())
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup.findAll('p')
    for line in tags:
        rawhand.write(str(line) + '. \n')
    
rawhand.close()