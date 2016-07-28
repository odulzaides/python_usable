#! /usr/bin/python

import sys
import re

pattern = re.compile(r".{1,3}\thttp.*")
outFile = open(sys.argv[2], "w")

with open(sys.argv[1]) as f:
    for line in f :
        if (pattern.match(line)):
            url = line.split()[1]
            outFile.write(url+"\n") 

## USAGE skytapExtractLinks.py input-file output-file
 
