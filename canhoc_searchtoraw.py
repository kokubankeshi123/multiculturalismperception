import os
import re
import urllib
from BeautifulSoup import *

# open "canhoc_rawtext2.txt" in the writing mode
f = open('canhoc_rawtext2.txt', 'w')
path = 'C:/Users/Keitaro/Documents/University of Toronto/MA-Political Science/MRP/textmining/canadahansard/hoc'
files = os.listdir(path)
for file in files:
    # rewrite "file" to be a full pass
    file = "/".join([path, file])
    hand = open(file)
    data = hand.read()
    data = data.replace('\n', ' ')
    data = data.replace('\r', ' ')
    soup = BeautifulSoup(data)
    tags = soup.findAll('div', attrs = {'class':'para'})
    for line in tags:
        f.write(str(line) + '. \n')
f.close()
