#! /usr/bin/python

import sys
import os

dirDel = sys.argv[1]

mapped = r'/gpfs/ddn/srm/cms//store/user/lmartini/' + dirDel + r'/'

fileList =  os.listdir(mapped)



# print "Directory to be deleted: ", dirIn



for file in fileList:
    rmString = r'srmrm -2 "srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/user/lmartini/' + dirDel + r'/' + file + r'"'
    print rmString
    os.system(rmString)

rmDirString = r'srmrmdir -2 "srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/user/lmartini/' + dirDel + r'"'

print rmDirString
os.system(rmDirString)
    
