import os
import glob
import re
import eyed3

directories = glob.glob("/Users/lucamartini/Music/cinese tradizionale/")

for directory in directories:
    files = glob.glob(directory + "*.mp3")
    for file in files:
        basename = os.path.basename(file)
        dirname = os.path.dirname(file)

        reg = r'(.+).mp3'
        searched = re.search(reg, basename)
        newtitle = searched.group(1)
        audiofile = eyed3.load(file)
        print 'new:', file
        # print 'old: ', basename, '; title:', audiofile.tag.title
        audiofile.tag.title = newtitle.decode('unicode-escape')
        audiofile.tag.album = u'traditional chinese'
        print 'title:', audiofile.tag.title
        audiofile.tag.save()


 iladad
