import random         
          
    
def qws():
    with open('words1.txt','r', encoding = 'utf-8') as ws1:
        wss1=[]
        for line in ws1:
            line = line.strip()
            wss1.append(line)
    return random.choice(wss1)

def wws():
    with open('words2.txt','r', encoding = 'utf-8') as ws2:
        wss2=[]
        for line in ws2:
            line = line.strip()
            wss2.append(line)
    return random.choice(wss2)
    
def ews():
    with open('words3.txt','r', encoding = 'utf-8') as ws3:
        wss3=[]
        for line in ws3:
            line = line.strip()
            wss3.append(line)
    return random.choice(wss3)

def verb():
    with open('words2v.txt','r', encoding = 'utf-8') as ws2v:
        wss2v=[]
        for line in ws2v:
            line = line.strip()
            wss2v.append(line)
    return random.choice(wss2v)

def p51():
   
    pros=random.choice([1, 2, 3])
    if pros == 1:
        return qws()+' '+wws()+' '+verb()
    elif pros == 2:
        return verb()+' '+wws()+' '+qws()
    else:
        return wws()+' '+qws()+' '+verb()



def p52():
    pr=random.choice([1, 2])
    if pr == 1:
        return ews()+' '+verb()
    else:
        return verb()+' '+ews()
    

def p5():
    prost = random.choice([1, 2])
    if prost == 1:
        return p51()  
    else:
        return p52()   

def very():
    with open('ochen.txt','r', encoding = 'utf-8') as och:
        oche=[]
        for line in och:
            line = line.strip()
            oche.append(line)
    return random.choice(oche)

def red():
    with open('adjn.txt','r', encoding = 'utf-8') as adj:
        adjs=[]
        for line in adj:
            line = line.strip()
            adjs.append(line)
    return random.choice(adjs)
def plat():
    with open('pla.txt','r', encoding = 'utf-8') as pla:
        plas=[]
        for line in pla:
            line = line.strip()
            plas.append(line)
    return random.choice(plas)

def znak():
    zn = [".", "!", "..."]
    return random.choice(zn)
    
def p7():
    return very()+' '+red()+' '+plat()+znak()

def maybe():
    with open('maybe.txt','r', encoding = 'utf-8') as may:
        be=[]
        for line in may:
            line = line.strip()
            be.append(line)
    return random.choice(be)

def sun():
    with open('pla.txt','r', encoding = 'utf-8') as suns:
        sunn=[]
        for line in suns:
            line = line.strip()
            sunn.append(line)
    return random.choice(sunn)

def fin():
    with open('fin.txt','r', encoding = 'utf-8') as vse:
        vses=[]
        for line in vse:
            line = line.strip()
            vses.append(line)
    return random.choice(vses)



def last():
    return maybe()+', '+sun()+' '+fin()
    
def poem():
    print (p5())
    print (p7())
    print (p5())
    print (p7())
    print (last())

poem()
