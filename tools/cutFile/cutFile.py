#!/usr/bin/python
#coding=utf-8

import sys

def usage():
    print "%prog <filename> <cutNum>"

def main():
    if(len(sys.argv)) != 3:
        usage()
        return

    filenameIn = sys.argv[1]
    filenameOut = '_out_' + filenameIn
    cutNum = int(sys.argv[2])
    print "Output file:  %s" % filenameOut 

    fpIn = open(filenameIn, 'r')
    fpOut = open(filenameOut, 'w')
    
    while True:
        str1 = fpIn.readline()
        
        if len(str1) < 1:
            break

        str2 = str1[cutNum:]
        fpOut.write(str2)

    fpIn.close()
    fpOut.close()

if __name__ == "__main__":
    main()
