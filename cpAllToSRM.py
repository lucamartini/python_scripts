#! /usr/bin/python

import sys
import os

dirIn = os.path.abspath(sys.argv[1])
dirOut = sys.argv[2]

print "Input dir: ", dirIn
print "Output dir: ", dirOut

fileList =  os.listdir(sys.argv[1])

for file in fileList:
    cpString = r'lcg-cp -b -D srmv2 file:///' + dirIn + r'/' + file + r' "srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/user/lmartini/' + dirOut +r'/' + file + r'"'
    print cpString
    os.system(cpString)
    




