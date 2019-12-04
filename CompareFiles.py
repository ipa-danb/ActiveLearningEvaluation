import os
a=[]
b=[]
i=0
k=0
currentimg = '"test10.png"'
f= open("groundTruth.csv","r+")
y = f.readline()
while y is not '':
    y=f.readline()
    x=y.split(',')
    print(x)
    if currentimg == x[0]:
        a.append([x[0],float(x[1])+float(x[3]),float(x[2])+float(x[4]),x[5]])
    else:       
        b.append(a)
        a=[]
        currentimg=x[0]
        k+=1

#print(b)

a=[]
c=[]
i=0
k=0
currentimg = '"test10.png"'
f= open("evaluate-export302.csv","r+")
y=f.readline()
while y is not '':
    y=f.readline()
    x=y.split(',')
    if currentimg == x[0]:
        a.append([x[0],float(x[1])+float(x[3]),float(x[2])+float(x[4]),x[5]])
    else:
        c.append(a)
        a=[]
        currentimg=x[0]
        k+=1



new_file = "evaluate-export1501.csv"

