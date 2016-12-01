with open('textr.txt', 'r', encoding = 'utf-8') as t:
    fiveword=0
    numline=0
    print(t.read)
    
    for line in t:
        words=[]
        words=line.split(' ')
        if len(words)>5:
            fiveword+=1
        numline+=1
print (fiveword)
print ('Кол-во строк:', numline)
print ('В файле '+str(int(((fiveword/numline)*100)//1))+'% строк, в которых больше пяти слов')
