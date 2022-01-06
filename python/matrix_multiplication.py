n=int(input())
A=[]
B=[]
for i in range(n):
    a=[]
    a=input().split(',') 
    A.append(a)
for i in range(n):
    a=[]
    a=input().split(',') 
    B.append(a)
for i in range(n):
    for j in range(n):
        c=0
        for k in range(n):
            c=c+int(A[i][k])*int(B[k][j])
        print(c,sep=',')
    print("")