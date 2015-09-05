import os
import re
# open "urlresult.txt" in the appending mode
f = open('urlresult.txt', 'a')
path = 'C:/Users/Keitaro/Documents/University of Toronto/MA-Political Science/MRP/textmining/australiahansard/searchresults'
files = os.listdir(path)
for file in files:
    # rewrite "file" to be a full pass
    file = "/".join([path, file])
    hand = open(file)
    for line in hand:
        x = re.findall('<div class="sumLink"><a href="(http://parlinfo\S*)"' , line)
        if len(x) > 0:
            f.write(str(x)+',,')
f.close()

f1 = open('urlresult.txt', 'r')
f2 = open('aus_urls.txt', 'a')
for line in f1:
    line = line.replace("[", "")
    line = line.replace("]", "")
    line = line.replace("'", "")
    f2.write(str(line))
f1.close()
f2.close()

os.remove("urlresult.txt")