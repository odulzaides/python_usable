#! /usr/bin/python
##
## USAGE skytapExtractLinks.py input-file output-file
##

import sys
import re

###     Chose file output type

print "1.   Javascript Object in a JS File."
print "2.   JSON format in a JSON File."
print "3.   Extract the links to a Plain Text File."
format = raw_input("What output format would you like? " )

##  Convert to format type chosen
if format == "1":
    inFile = sys.argv[1]
    outFileName = inFile.split('.')
    outFile = open(outFileName[0] + '.js' , "w")
    pattern = re.compile(r".{1,3}\thttp.*")


    with open(sys.argv[1]) as f:
        outFile.write('VMs = {' + "\n")

        # Set up vm host numbers. ### -  vm0 is ALL vms
        i = 0
        # Write the Skytap links and vm# to JSON file
        for line in f:
            if (pattern.match(line)):   
                url = line.split()[1]
                outFile.write('vm{}'.format(i) + ':' + '"' + url+'",' + "\n")
                i = i + 1 
        outFile.write('}') 

elif format == "2":
    inFile = sys.argv[1]
    outFileName = inFile.split('.')
    pattern = re.compile(r".{1,3}\thttp.*")
    outFile = open(outFileName[0] + '.json' , "w")

    with open(sys.argv[1]) as f:
        outFile.write('{' + "\n")

        # Set up vm host numbers. ### -  vm0 is ALL vms
        i = 0
        # Write the Skytap links and vm# to JSON file
        for line in f:
            if (pattern.match(line)):   
                url = line.split()[1]
                outFile.write('"vm{}'.format(i) + '"' + ':' + '"' + url+'",' + "\n")
                i = i + 1 
        outFile.write('},')

elif    format == "3":
    inFile = sys.argv[1]
    outFileName = inFile.split('.')
    pattern = re.compile(r".{1,3}\thttp.*")
    outFile = open(outFileName[0] + '-EXTRACTED.txt' , "w")

    with open(sys.argv[1]) as f:
        for line in f :
            if (pattern.match(line)):
                url = line.split()[1]
                outFile.write(url+"\n") 
