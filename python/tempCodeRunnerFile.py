n=int(input())
arr = []
for i in range(0,n+1):
    ele = int(input())
    arr.append(ele)
arr.sort()
print("The Runner-up score is : ", arr[-2])