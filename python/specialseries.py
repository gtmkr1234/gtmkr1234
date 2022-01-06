n=int(input())
sum2=0
for i in range(1,n+1):
    sum1=0
    for j in range(1,i+1):
        sum1 = sum1 + j
    sum2 = sum2 + sum1
print(sum2)