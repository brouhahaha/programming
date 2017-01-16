##срабатывало только через вызов функции perc c числовым аргументом, простозапущенная программа на введенные данные не даёт никакой реакции
def filename():
    fname=input('Введите имя файла ')
    return fname

def opentext ():
    with open (filename(), 'r', encoding='utf-8') as f:
        text=f.read()
    textl=text.lower() 
    ws = textl.split() 
    tekst=[] 
    for w in ws:
        wstr=w.strip('!?.,:;()') 
        tekst.append(wstr) 
    return tekst 

def unws(tekst):
    text=tekst
    unws=[]
    for w in text:
        if w[0:2]=='un':
            unws.append(w)
    return unws

def nunws(unws):
    return len(unws)

def perc (num):
    ws=opentext()
    longw=[]
    for w in unws(ws):
        if len(w)>num:
            longw.append(w)
    return str(int(len(longw)/nunws(unws(ws))*100))+'%'

perc(int(input('Введите число ')))
