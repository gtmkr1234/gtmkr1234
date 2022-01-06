n=int(input())
last=int(n**(1/2))+1
pc=0
for i in range(2,last):
    if n%i==0:
        pc+=1
if (pc==0):
    print("PRIME")
else:
    print("NOTPRIME")