#! /usr/bin/python

import sys
import os
import re

from subprocess import check_output
from subprocess import call

ls = "lcg-ls"

input = "srm://gridsrm.ts.infn.it//cms/store/user/casarsa/PR/SingleMuonPU140/"

output_dir = "srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/user/lmartini/AM/AfterPatternRecognition/"

cp = "lcg-cp"
opt_b = "-b"
opt_D = "-D"
opt_v2= "srmv2"
opt_v = "-v"

files = check_output([ls, input])
fileList = files.split("\n")
fileList.pop()

for file in fileList:
    searched = re.search(r'[a-zA-Z0-9/.:]*/([a-zA-Z0-9_.]+)$', file)
    filename = searched.group(1)
    input_file = '"' + input + filename + '"'
    output_file = '"' + output_dir + filename + '"'
    command = [cp,
           #    opt_b,
               opt_D, opt_v2,
               opt_v,
               input_file, output_file]
    #print command
    #call(command)
    s = " ".join(command)
    os.system(s)
    #print(s)
