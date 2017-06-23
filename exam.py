import os
import re

def preprocessing (content):
    notags = re.sub(r'\<[^>]*\>', '',content)
    nons = re.sub (r'\n', '', notags)
    return nons
                
def countsen ():
    for root, dirs, files in os.walk(os.path.join(os.getcwd(), 'news')):
        for f in files:
            with open (os.path.join(root, f), 'r', encoding='Windows-1251')as n:
                content = n.read()
                content1 = preprocessing(content)
                numsen = content1.split('.')
                num = str(len(numsen))
                template = "{}\t{}\n"
                with open('numsens.txt', 'a', encoding='utf-8') as k:
                        k.write(template.format(f, num))
countsen()

def author():
    for root, dirs, files in os.walk(os.path.join(os.getcwd(), 'news')):
        for f in files:
            with open (os.path.join(root, f), 'r', encoding='Windows-1251')as n:
                content = n.read()
                content1 = preprocessing(content)
                words = content1.split(' ')
                author = words [0]+' '+words[1]
                name = f
                topic = re.search(r'<meta content=".*" name="topic"/>', content)
                with open('table.csv', 'a', encoding='Windows-1251') as k:
                    k.write(name+author)
                        
author()
