st=input()
x,y=0,0
if st=="START":
    while st!= "STOP":
        st=input()
        if st=="UP":
            x+=1
        elif st=="DOWN":
            x-=1
        elif st=="LEFT":
            y-+1
        elif st=="RIGHT":
            y+=1
    print(abs(x)+abs(y))
