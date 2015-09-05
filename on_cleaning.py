import re

rawhand = open('on_rawtext.txt', 'r')
cleanhand = open('on_cleantext.txt', 'w')

rawdata = rawhand.read()
cleandata = str(rawdata)
cleandata = cleandata.replace('\n', ' ')
cleandata = cleandata.replace('\r', ' ')
cleandata = cleandata.replace('Hon.', 'Hon ')
cleandata = cleandata.replace('Mr.', 'Mr ')
cleandata = cleandata.replace('Ms.', 'Ms ')
cleandata = cleandata.replace('St.', 'St ')

cleandata = re.sub('<b>.+?</b>', ' ', cleandata)

cleandata = re.sub('<\S+?>', ' ', cleandata)
cleandata = re.sub('<\S+?\s\S+?>', ' ', cleandata)
cleandata = re.sub('<\S+?\s\S+?\s\S+?>', ' ', cleandata)
cleandata = re.sub('<\S+?\s\S+?\s\S+?\s\S+?>', ' ', cleandata)
cleandata = re.sub('<\S+?\s\S+?\s\S+?\s\S+?\s\S+?>', ' ', cleandata)

cleandata = cleandata.replace('&quot;', ' ')
cleandata = cleandata.replace('!', '.')
cleandata = cleandata.replace('?', '.')

cleandata = cleandata.split('.')

# remove empty elements
while cleandata.count("") > 0:
    cleandata.remove("")

# extract unique elements in the list
cleandata = list(set(cleandata))

for line in cleandata:
    if line.find('Multiculturalism') == -1 and line.find('multiculturalism') == -1: continue
    cleanhand.write(str(line) +'. \n')
    
rawhand.close()
cleanhand.close()