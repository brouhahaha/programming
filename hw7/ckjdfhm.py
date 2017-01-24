import random
def opendict():
    d={} 
    with open ('dict.csv', 'r', encoding='utf-8') as f:
        text = f.readlines()
        for p in text:
            prs=[]
            pr=p.strip('\n')
            prs=p.split()
            d[prs[0]]=prs[1]
    return d 

def zag():
    d=opendict()
    klus=[]
    for key in d:
        klus.append(key)
    klu=random.choice(klus)
    print('отгадай-ка слово:', klu,'...')
    return klu

def good():
    with open ('good.txt', 'r', encoding='utf-8') as f:
        text = f.readlines()
        well=random.choice(text)
        return print(well)

def oops():
    with open ('false.txt', 'r', encoding='utf-8') as f:
        text = f.readlines()
        false=random.choice(text)
        return print(false)
    
def otvet():
    klu=zag()
    d=opendict()
    slovo=input('ответ:')
    if slovo==d[klu]:
        return good()
    else:
        return oops()
    
otvet()
