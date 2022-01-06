#PPA WEEK 6
a=input()
if (len(a)%2==0):
    if(a.endswith(".")):
        a=a[:-1]
    else:
        a=a+"."
l=(len(a)//2)+1
substring=a[(l-2):(l+1)]
print(substring)