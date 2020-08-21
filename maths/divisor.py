#!/usr/bin/python
#coding=utf-8

import sys

def usage():
  print "divisor <Num>"

########################################################################
# function name: main
########################################################################
def main():
  if(len(sys.argv)) != 2:
    usage()
    return
  
  try:
    N = int(sys.argv[1])
  except:
    print("Invalid number:" + sys.argv[1])
    return
  else:
    if N <= 0:
      print("Invalid number: %d" % N)
      return
    else:
      arrRange = range(1, N+1)
      arrDivisor = []
      iSum = 0
      iProd = 1
      for i in arrRange:
        if N % i == 0:
          arrDivisor.append(i)
          iSum += i
          iProd *= i
      print(arrDivisor)
      print("Total divisors: %d" % len(arrDivisor))
      print("Sum: %d" % iSum)
      print("Product: %d" % iProd)


if __name__ == "__main__":
  main()