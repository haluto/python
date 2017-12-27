#!/usr/bin/python
# -*- coding: UTF-8 -*-


##os.system
#该方法是直接调用标准C的system() 函数，仅仅在一个子终端运行系统命令，而不能获取命令执行后的返回信息。
#os.system("adb root")

##os.popen
#该方法不但执行命令还返回执行后的信息对象，是通过一个管道文件将结果返回。
#output = os.popen("adb devices")
#print output.read()

##commands.getstatusoutput
#import commands
#(status, output) = commands.getstatusoutput("cat /proc/cpuinfo")
#print status, output


import sys
import os
import xml.etree.ElementTree as ET


########################################################################
# CommandItem class
########################################################################
class CommandItem:
    __name = ''
    __property = ''
    __valueon = 0
    __valueoff = 0
    __keyword = ''
    __description = ''

    def __init__(self, name, prop, valueon, valueoff, keyword, description):
        self.__name = name
        self.__property = prop
        self.__valueon = valueon
        self.__valueoff = valueoff
        self.__keyword = keyword
        self.__description = description

    def name(self):
        return self.__name
    def prop(self):
        return self.__property
    def valueon(self):
        return self.__valueon
    def valueoff(self):
        return self.__valueoff
    def keyword(self):
        return self.__keyword
    def description(self):
        return self.__description

########################################################################
# function name: readxml
# return: list of commandItem
########################################################################
def readxml():
    tree = ET.parse('info.xml')
    root = tree.getroot()

    commandList = []
    for command in root.findall('command'):
        name = command.get('name')
        prop = command.find('property').text
        valueon = command.find('valueon').text
        valueoff = command.find('valueoff').text
        keyword = command.find('keyword').text
        description = command.find('description').text

        commandItem = CommandItem(name, prop, valueon, valueoff, keyword, description)
        commandList.append(commandItem)

    return commandList
'''
    for child in root:
        print child.tag, child.attrib

    for property in root.iter('property'):
        print property.text

    for command in root.findall('command'):
        property = command.find('property').text
        name = command.get('name')
        print name, property
'''

########################################################################
# function name: usage
########################################################################
def usage():
    print '''
Usage:  camdebug --help(-h)  -> to show supported commands.
        camdebug <command>   -> to run supported command.
    '''


########################################################################
# function name: help
########################################################################
def help(commandList):
    for item in commandList:
        print item.name()
        print "        ", item.description().replace('"', '')
        print "        ", "Set %s to enable, set %s to disable." % (item.valueon(), item.valueoff())


########################################################################
# function name: has_device
# return: True if has device, False if no device.
########################################################################
def has_device():
    output = os.popen("adb devices")
    str = output.read()
    hasDevice = str.rstrip().endswith("device")

    if (not hasDevice):
        print "No device connected, please connect your device first."

    return hasDevice
    

########################################################################
# function name: is_cmd_in_commandList
# return: True if cmd is in commandList, False if not.
########################################################################
def is_cmd_in_commandList(cmd, commandList):
    for item in commandList:
        if item.name() == cmd:
            return True

    return False


########################################################################
# function name: run_command
########################################################################
def run_command(cmd, commandList):

    needRun = False

    if (has_device()):
        os.popen("adb root") 
        output = os.popen("adb root") # tricky, double call to make sure to get output of "adb root"
        outStr = output.read()
        if (outStr.find("already running as root") > 0):
            needRun = True

    if (needRun):
        for item in commandList:
            if item.name() == cmd:
                #item.prop().replace('"','') is to remove " in string.
                cmdStr = "adb shell setprop " + item.prop().replace('"','') + " " + item.valueon()
                print cmdStr
                os.popen(cmdStr)

                #check result
                cmdStr = "adb shell getprop " + item.prop().replace('"','')
                output = os.popen(cmdStr)
                outStr = output.read()
                if (outStr.rstrip() == item.valueon()):
                    print "Set property succeeded."
                    print "You can grep %s as keyword for %s to check the log now." % (item.keyword(), item.name()) 
                else:
                    print "Set property failed."
                break


########################################################################
# function name: main
########################################################################
def main():
    
    if (len(sys.argv) == 2):
        commandList = readxml()
        if (sys.argv[1] == "--help" or sys.argv[1] == "-h"):
            help(commandList)
        elif (is_cmd_in_commandList(sys.argv[1], commandList)):
            print "OK, %s is supported" % sys.argv[1]
            run_command(sys.argv[1], commandList)
        else:
            print "Sorry, %s is not supported." % sys.argv[1]
    else:
        usage()

if __name__ == '__main__':
    main()



