P = 13
p = list(range(1,P))
n = 1
for i in range(len(p)):
    n*=p[i]
n = (n+1)/(P*P)
o = int(n)
if o == n:
    print(True)
else:
    print(False)
