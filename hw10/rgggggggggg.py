import re
pti=r'птиц'
ppti=r'Пт[ии́]ц'
fish=r'рыб'
ffish=r'Рыб'
ptiey=r'птицей'
pptiey=r'Птицей'
fishy=r'рыбой'
ffishy=r'Рыбой'
def cont():
    with open('birds.html', 'r', encoding = 'utf-8') as f:
        content=f.read()
        return content

def text():
    birds=cont()
    ryba=re.sub(pti,fish, birds)
    birds=re.sub(ppti,ffish,ryba)
    ryba=re.sub(ptiey,fishy,birds)
    birds=re.sub(pptiey,ffishy,ryba)
    return birds

def save():
    new=text()
    with open('ryby.txt', 'w', encoding = 'utf-8') as n:
    	n.write(new)
    	return new
    

save() 

## не меняется форма в начале статьи - та, что с ударением, не понимаю, почему
