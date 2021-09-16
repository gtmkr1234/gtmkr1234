n=int(input("Enter the number"))
b=int(n**0.5)
for i in range(2,b+1):
    if n%i!=0:
        print("Number is prime")
    else :
        break
else :
    print("Number is not prime")