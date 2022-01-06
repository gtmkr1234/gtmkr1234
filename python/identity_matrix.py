n=int(input())
for i in range(n):
    for j in range(n-1):
        if(i==j):
            print('1', end=',')
        else:
            print('0',end=',')
    if((n-1)==i):
        print('1')
    else:
        print('0')