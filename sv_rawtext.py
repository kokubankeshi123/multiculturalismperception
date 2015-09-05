import re
import urllib
from BeautifulSoup import *

# open the "qc_urls.txt" in the reading mode
urlhand = open('sv_urls.txt', 'r')
data = urlhand.read()
lst = data.rsplit(',')
# remove empty elements
while lst.count("") > 0:
    lst.remove("")

rawhand = open('sv_rawtext.txt', 'w')

for url in lst:
    url = str(url.strip())
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup.findAll(['div', 'pre'])
    for line in tags:
        rawhand.write(str(line) + '. \n')
    
rawhand.close()