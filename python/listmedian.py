marks=[3,2,1,5,4]
sorted_L=[]
while(len(marks)>0):
    m=marks[0]
    for i in marks:
        if m<=i:
            m=i
    sorted_L.append(m)
    marks.remove(m)
a=len(sorted_L)
if a%2==0:
    median=sorted_L[int(a/2)-1]+sorted_L[int((a/2)+1)-1]
else:
    median=sorted_L[int((a+1)/2)-1]
print(median)