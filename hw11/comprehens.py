import re

def text():
    with open('text.txt', 'r', encoding = 'utf-8') as f:
        f = f.read()
        f=f.lower()
        sens = re.split('[.\?!] ',f)
        sens1 = [re.sub (r'[,.()?!:;-]', '', sen) for sen in sens ]
        sens_new = [ sen.split(' ') for sen in sens1 ]
        return sens_new
    
    
def word_num():
    sens = text()
    number = {word: sen.count(word) for sen in sens for word in sen}
    flat = [word for sen in sens for word in sen]
    for word in flat:
        if flat.count(word)>1:
            flat.remove(word)
    for word in flat:
        if  number[word]>1:
                print(word, '{:^10}'.format(number[word]))
        
word_num()
