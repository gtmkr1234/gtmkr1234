n=input().split(',')
i=len(n)-1
fl=[]
while(i>=0):
    fl.append(n[i])
    i=i-1
print(','.join(fl))