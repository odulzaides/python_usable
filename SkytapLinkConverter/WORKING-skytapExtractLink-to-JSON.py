#! /usr/bin/python
##
## USAGE skytapExtractLinks.py input-file output-file
##

import sys
import re

pattern = re.compile(r".{1,3}\thttp.*")
outFile = open(sys.argv[2], "w")

with open(sys.argv[1]) as f:
    outFile.write(str(vm_count) +  "\n")
    outFile.write('{' + "\n")

    # Set up vm host numbers. /// vm0 is ALL vms
    i = 0
    # Write the Skytap links to JSON file
    for line in f:
        if (pattern.match(line)):   
            url = line.split()[1]
            outFile.write('"vm{}'.format(i) + '"' + ':' + '"' + url+'"' + "\n")
            i = i + 1 
    outFile.write('}')
    
    


