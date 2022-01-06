a="ABCDEFGH"
b="12345678"
start=input()
end=input()
logic=abs(a.index(start[0])-a.index(end[0])) == abs(b.index(start[1])-b.index(end[1]))
if logic:
    print("YES")
else:
    print("NO")