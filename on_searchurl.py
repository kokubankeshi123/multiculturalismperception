import re
import os
import urllib
from BeautifulSoup import *

# open the text file
datahand = open('urldata.txt', 'w')
# for loop
for n in range(1,32):
    url = 'http://hansardindex.ontla.on.ca/H2vers2.asp?pagestring=(@contents%20multiculturalism)&scroll=' + str(n) + '&stp=1'
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    psoup = soup.findAll('p')
    for element in psoup:
        data = element.findAll('a')
        datahand.write(str(data))
datahand.close()

datahand = open('urldata.txt', 'r')
urlhand = open('on_urls.txt', 'w')

rawdata = datahand.read()
cleandata = re.findall('<a href(=".*?">)', rawdata)
for line in cleandata:
    if line.find('hansardeissue') == -1 : continue
    line = line.replace('="', 'http://hansardindex.ontla.on.ca')
    line = line.replace('">', ',')
    urlhand.write(line)

datahand.close()
urlhand.close()

os.remove("urldata.txt")