n = 25
h = int(n**0.5)
if n/h == h :
    n = n + 2*h+1
    print(n)
else:
    print(-1)