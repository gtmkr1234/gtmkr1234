n=input().split(' ')
query=input()
if query in n:
    print("YES")
    print(n.count(query))
else:
    print("NO")