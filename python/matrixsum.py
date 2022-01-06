n=int(input())
lst1=[]
lst2=[]
for i in range(n):
    a=[]
    a=input().split(',') 
    lst1.append(a)
for i in range(n):
    a=[]
    a=input().split(',') 
    lst2.append(a)
for i in range(n):
    for j in range(n-1):
        s=int(lst1[i][j])+int(lst2[i][j])
        print(s, end=',')
    print(int(lst1[i][-1])+int(lst2[i][-1]))