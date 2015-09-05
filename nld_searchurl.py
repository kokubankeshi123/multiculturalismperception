import re
from BeautifulSoup import *

# open the "searchresults.txt" in the reading mode
searchhand = open('nld_searchresults.txt', 'r')
urlhand = open('nld_urls.txt', 'w')

soup = BeautifulSoup(searchhand)
tags = soup('a')
for tag in tags:
    link = tag.get('href', None)
    urlhand.write(str('https://zoek.officielebekendmakingen.nl/' + link + ',') )

searchhand.close()
urlhand.close()