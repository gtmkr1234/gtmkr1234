x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
x3=float(input())
if(x1==x2 or y1==y2):
    if(x1==x2):
        print("Vertical Line")
    elif(y1==y2):
        print("Horizontal Line")
else :
    y3=(((x3-x1)*(y2-y1))/(x2-x1))+y1
    slope=(y2-y1)/(x2-x1)
    print(y3)
    if(slope>0):
        print("Positive Slope")
    else:
        print("Negative Slope")