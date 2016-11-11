a=[]
for i in range (8):
        a.append(input())
b=[]
for i in range (0,7,2):
        b.append(a[i])
        b.append(a[i+1])
        print (''.join(b))
        b=[]
