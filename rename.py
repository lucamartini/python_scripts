import os
import glob
import re

directories = glob.glob("/Users/lucamartini/Music/Chinese_Ancient_Music_08_CD/*/")

for directory in directories:
    files = glob.glob(directory + "*.mp3")
    for file in files:
        basename = os.path.basename(file)
        dirname = os.path.dirname(file)
        regdir =  r'[a-zA-Z0-9/_.]*/([a-zA-Z0-9_. -]+)'
        searcheddir = re.search(regdir, dirname)
        #print searcheddir.group(1)
        #print basename
        reg = r'([0-9][0-9]) Various - (.*) - (.+)'
        searched = re.search(reg, basename)
        newname = searched.group(1) + ' - ' + searched.group(3)
        newfile = dirname + '/' + newname
        #print 'old: ', file
        #print 'new: ', newfile
        os.rename(file, newfile)
