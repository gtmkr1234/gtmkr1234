s=str(input()).lower()
std='abcdefghijklmnopqrstuvwxyz'
op=''
for i in std:
    for j in s:
        if i==j:
            op+=j
print(op)