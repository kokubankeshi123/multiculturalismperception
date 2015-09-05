# -*- coding: utf-8 -*-
import re
import sys
import codecs

rawhand = codecs.open('sv_rawtext.txt', 'r', encoding = 'utf-8')
cleanhand = codecs.open('sv_cleantext.txt', 'w', encoding = 'utf-8')

rawdata = rawhand.read()
cleandata = unicode(rawdata)
cleandata = cleandata.replace('\n', ' ')
cleandata = cleandata.replace('\r', ' ')

cleandata = re.sub('<b>.+?</b>', ' ', cleandata)

cleandata = re.sub('<\S+?>', ' ', cleandata)
cleandata = re.sub('<\S+?\s\S+?>', ' ', cleandata)
cleandata = re.sub('<\S+?\s\S+?\s\S+?>', ' ', cleandata)

cleandata = cleandata.replace('!', '.')
cleandata = cleandata.replace('?', '.')

cleandata = cleandata.split('.')

# remove empty elements
while cleandata.count("") > 0:
    cleandata.remove("")

# extract unique elements in the list
cleandata = list(set(cleandata))

key1 = u'Mångkultur'
key2 = u'mångkultur'

for line in cleandata:
    if line.find(key1) == -1 and line.find(key2) == -1: continue
    cleanhand.write(line +'.\n')
    
rawhand.close()
cleanhand.close()