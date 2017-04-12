import os
import re

allobj = os.listdir('.')
lat = r'[A-Za-z]'
kir = r'[А-Яа-я]'
folders = []
fold_new = []
folds = allobj

def fold_num():
    for f in folds:
        if os.path.isfile(f) == True:
            folds.remove(f)
        
    for fl in folds:
        if re.search(lat, fl) != None and re.search(kir, fl) != None:
            folders.append(fl)
    print ('папок, название которых содержит и кириллические, и латинские символы:', len(folders))

def norepeat():
    for obj in allobj:
        index = obj.rfind('.')
        if index != -1:
            obj = obj[:index]
        if fold_new.count(obj) == 0:
            fold_new.append(obj)
            print (obj)


    
fold_num()
norepeat()
