import re
import sys
import codecs

rawhand = codecs.open('qc_rawtext.txt', 'r', 'latin-1')
cleanhand = codecs.open('qc_cleantext.txt', 'w', 'latin-1')

rawdata = rawhand.read()
cleandata = unicode(rawdata)
cleandata = cleandata.replace('\n', ' ')
cleandata = cleandata.replace('\r', ' ')
cleandata = cleandata.replace('M.', 'M ')
cleandata = cleandata.replace('Mr.', 'Mr ')
cleandata = cleandata.replace('Ms.', 'Ms ')
cleandata = cleandata.replace('St.', 'St ')

cleandata = re.sub('<b>.+?</b>', ' ', cleandata)

cleandata = re.sub('<\S+?>', ' ', cleandata)
cleandata = re.sub('<\S+?\s\S+?>', ' ', cleandata)
cleandata = re.sub('<\S+?\s\S+?\s\S+?>', ' ', cleandata)
cleandata = re.sub('<\S+?\s\S+?\s\S+?\s\S+?>', ' ', cleandata)

cleandata = cleandata.replace('!', '.')
cleandata = cleandata.replace('?', '.')

cleandata = cleandata.split('.')

# remove empty elements
while cleandata.count("") > 0:
    cleandata.remove("")

# extract unique elements in the list
cleandata = list(set(cleandata))

for line in cleandata:
    if line.find('Multiculturalisme') == -1 and line.find('multiculturalisme') == -1: continue
    cleanhand.write(line +'.\n')
    
rawhand.close()
cleanhand.close()