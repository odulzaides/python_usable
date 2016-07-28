import os
dir = "/Volumes/Fileshare/IT_Data-on_Server/Videos/LYNDA.COM/LyndaVideos"
files = []
for i in os.listdir(dir):
    files.append(i)
### Use join to put the dir and file together.
### join uses a str and list.
### It puts the list item before the string
# print "Hi".join(l) give
# lHi
 
print len(files)
for i in files:
    print dir,i
    
