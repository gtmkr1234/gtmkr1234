a=input().lower()
final=""
if(a.count("a")!=0):
    final="a"
if(a.count("e")!=0):
    final+="e"
if(a.count("i")!=0):
    final+="i"
if(a.count("o")!=0):
    final+="o"
if(a.count("u")!=0):
    final+="u"
if final=="":
    print("none")
print(final)