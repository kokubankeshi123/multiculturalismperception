import re
import urllib
from BeautifulSoup import *

# open the "cansen_urls.txt" in the reading mode
urlhand = open('cansen_urls.txt', 'r')
data = urlhand.read()
lst = data.rsplit(',')

# remove empty elements
while lst.count("") > 0:
    lst.remove("")

# extract unique elements in the list
lst = list(set(lst))

# open the "cansen_rawtext2.txt" in the writing mode
rawhand = open('cansen_rawtext2.txt', 'w')

for url in lst:
    url = str(url.strip())
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup.findAll('p')
    for line in tags:
        rawhand.write(str(line) + '. \n')

urlhand.close()
rawhand.close()