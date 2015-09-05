import re
from BeautifulSoup import *

# open the "searchresults.txt" in the reading mode
searchhand = open('qc_searchresults.txt', 'r')
urlhand = open('qc_urls.txt', 'w')

soup = BeautifulSoup(searchhand)
tags = soup('a')
for tag in tags:
    link = tag.get('href', None)
    urlhand.write(str('http://www.assnat.qc.ca' + link + ',') )

searchhand.close()
urlhand.close()