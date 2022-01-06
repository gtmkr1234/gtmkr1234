n = int(input())
for i in range(2, n+1):
  flag = 0
  for j in range(2, i):
      if not i%j:
          flag = 1
  if flag != 1 and not n%i:
      print(i)