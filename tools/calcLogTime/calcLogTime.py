#!/usr/bin/python
#coding=utf-8


'''
python 中 time 有三种格式：

float,

struct tuple(time.struct_time 或 datetime.datetime),

str

 

常用的：

float --> struct tuple:   time.localtime( float )

struct time tuple --> str: time.strftime(format, struct time tuple)

str --> struct time tuple: time.strptime(str, format)

struct time tuple --> float : time.mktime(struct time tuple)

struct time tuple --> datetime: datetime(*time_tuple[0:6])

 

float --> datetime: datetime.datetime.fromtimestamp( float )

datetime --> str: datetime.strftime(format, datetime)

str --> datetime: datetime.strptime(str, format)

datetime --> struct time tuple: datetime.timetuple()
'''


import sys
import time


########################################################################
# function name: str2ms
# description: transfer string to time in ms.
# return: time in ms.
########################################################################
def str2ms(str, format='%d-%m %H:%M:%S'):
    #01-06 08:28:57.273 -> str
    #01-06 08:28:57 -> s
    s = str[:-4]
    #str --> struct time tuple
    t = time.strptime(s, format)
    #struct time tuple --> float
    ms1 = (time.mktime(t)) * 1000
    ms2 = int(str[-3:])
    return (ms1 + ms2)

def usage():
    print "%prog <log_file> <begin_tag> <end_tag>"

def main():
    if(len(sys.argv)) != 4:
        usage()
        return

    filename = sys.argv[1]
    begin_tag = sys.argv[2]
    end_tag = sys.argv[3]
    begin = 0
    end = 0
    found = False
    
    
    fp = open(filename, 'r')
    
    while True:
        str = fp.readline()
        
        if len(str) < 1:
            break
            
        if str.find(begin_tag) > 0:
            #01-06 08:28:57.273
            begin = str2ms(str[:18])
            
            #once find begin tag, try to find end tag then.
            while True:
                str = fp.readline()
                
                if len(str) < 1:
                    break
                    
                # if lose log, this is the second begin_tag without get an end_tag, so update begin.
                if str.find(begin_tag) > 0:
                    #01-06 08:28:57.273
                    begin = str2ms(str[:18])
                    continue
                    
                if str.find(end_tag) > 0:
                    end = str2ms(str[:18])
                    found = True
                    break
        
        #print begin, end
        if (found is True):
            print "%d  (end: %s)" % ((end - begin), str[:18])
        
        found = False
            
    fp.close()

if __name__ == "__main__":
    main()
