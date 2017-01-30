import re    
regsit=r"\bси(жу|ди((шь|м|те?)?)|е(л[и,а,о]?|ть|в(ш(и(й|е|х|ми?)?))|ая|е(й|е|му?|го)))?|я(т|щ(и(й|ми?|х|е)|е(е|й|го|му?)|ая|ую))\b"

def tekst():
    with open ('new.txt', 'r', encoding='utf-8') as f:
        text=f.readlines()
        found=[]
        for line in text:
            words=line.split()
            for word in words:
                wor=word.lower()
                wor=wor.strip(".,?!:;-")
                if re.search (regsit, wor)!=None and found.count(wor)==0:
                    found.append(wor)
                    print(wor)
            
tekst()
