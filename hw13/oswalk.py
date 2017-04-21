import os
import re

def maxfiles ():
    numfiles = 0
    name = ''
    for root, dirs, files in os.walk('.'):
        if len (files) > numfiles:
            numfiles = len (files)
            name = re.sub(r'.*/', '', root)
    print ('Больше всего файлов в папке:', name) 
            
maxfiles ()
