import re

rawhand = open('canhoc_rawtext2.txt', 'r')
cleanhand = open('canhoc_cleantext2.txt', 'w')

rawdata = rawhand.read()
cleandata = str(rawdata)
cleandata = cleandata.replace('\n', ' ')
cleandata = cleandata.replace('\r', ' ')
cleandata = cleandata.replace('Hon.', 'Hon ')
cleandata = cleandata.replace('hon.', 'hon ')
cleandata = cleandata.replace('Mr.', 'Mr ')
cleandata = cleandata.replace('Ms.', 'Ms ')
cleandata = cleandata.replace('St.', 'St ')

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

for line in cleandata:
    line = line.strip()
    if line.find('Multiculturalism') == -1 and line.find('multiculturalism') == -1: continue
    cleanhand.write(str(line) +'. \n')

rawhand.close()
cleanhand.close()