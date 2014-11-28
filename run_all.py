#!/cvmfs/cms.cern.ch/slc6_amd64_gcc472/cms/cmssw-patch/CMSSW_6_2_0_SLHC20_patch1/external/slc6_amd64_gcc472/bin/python

import re
import os
import subprocess

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = newPath

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

pr_sector_script = "pr_runsector_mio.sh"

with open('banks.txt', 'r') as file:
    for line in file:
        print line
        ID = line.split("\t")[0]
        bankname = line.split("\t")[1]
        
        searched = re.search(r'620_SLHC7_MUBANK_lowmidhig_sec([0-9]+)[a-zA-Z0-9_]*([0-9]+)\.pbk$', bankname)
        sec = int(searched.group(1))
        thresh = int(searched.group(2)) - 1

        if (sec < 7 or sec > 40):
            missinghits = 1
        else:
            missinghits = 0
        
        subprocess.call(["mkdir", "-p", "ID"+ID])
        subprocess.call(["cp", pr_sector_script, "ID"+ID])

        with cd("ID"+ID):
            subprocess.call(["chmod", "+x", pr_sector_script])
            subprocess.Popen(["nohup", "./"+pr_sector_script, str(sec), str(missinghits), str(thresh), ID, bankname])
           
            
            
        
