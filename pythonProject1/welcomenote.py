# cook your dish here
n = int(input())
l = []
for i in range(n):
    x, y = map(int, input().split(' '))
    if y > x:
        l.append(abs(x - y) - 1)
    else:
        l.append(y)
for res in l:
    print(res)
