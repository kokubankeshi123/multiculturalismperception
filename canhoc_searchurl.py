import os
import re
# open "urlresult.txt" in the appending mode
f = open('urlresult.txt', 'a')
path = 'C:/Users/Keitaro/Documents/University of Toronto/MA-Political Science/MRP/textmining/canadahansard/hoc'
files = os.listdir(path)
for file in files:
    # rewrite "file" to be a full pass
    file = "/".join([path, file])
    hand = open(file)
    for line in hand:
        x = re.findall('(http://www\.parl\.gc\.ca/HousePublications/\S*)' , line)
        if len(x) > 0:
            x = str(x)
            x = x.replace('">', '')
            x = x.replace('"', '')
            f.write(x + ',')
f.close()

f1 = open('urlresult.txt', 'r')
f2 = open('canhoc_urls.txt', 'a')
for line in f1:
    line = line.replace("[", "")
    line = line.replace("]", "")
    line = line.replace("'", "")
    f2.write(str(line))
f1.close()
f2.close()

os.remove("urlresult.txt")