import re
reg=r'(<th style.*?title="(ISO \d{3})">(\2-\d))'


def find():
    with open('lang.html', 'r', encoding = 'utf-8') as f:
        content=f.read()
        isos=re.findall(reg, content)
        return isos

def save():
    isos=find()
    with open('isos.txt', 'w', encoding = 'utf-8') as n:
        for iso in isos:
            n.write(iso[2] + '\n')
        
save() 
