def cpdint(p,n):
    if n==1:
        return p*1.1
    else :
        return cpdint(p,n-1)*1.1

print(cpdint(1000,2))