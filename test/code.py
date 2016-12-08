with open('freq.txt', 'r', encoding = 'utf-8') as f:
    print ('Задание 1')
    for line in f:
        form = []
        form = line.split(' | ')
        if form[1] =='союз':
            print (' | '.join(form))


with open('freq.txt', 'r', encoding = 'utf-8') as f:
    sum=0
    fem = []
    morp = []
    print ('Задание 2')
    for line in f:
        form = []
        form = line.split(' | ')
        morp = form[1].split(' ')
        if len(morp)>2:
            if morp[2]=='ед' and morp[3]=='жен':
                fem.append(form[0])
                sum += float(form[2])
    print (', '.join(fem))
    print('Сумма ipm:', sum)


    
            
