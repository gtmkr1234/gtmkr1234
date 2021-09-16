n=int(input("Enter the number"))
if n in range(1,51):
    if n%3==0 and n%5==0:
       print("TIC-TAC")
    elif n%3==0:
       print("TIC")
    elif n%5==0:
       print("TAC")
else:
    print("Numbers are not in range of 1 to 50")