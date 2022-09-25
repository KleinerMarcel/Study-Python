a = int(input())
b = int(input())
if a<b :
    l = range(a,b)
    print(sum(list(l))+b)
else:
    l = range(b,a)
    print(sum(list(l))+a)