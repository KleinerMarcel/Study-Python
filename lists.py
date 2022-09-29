n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
m = max(n)
f = 0
for i in n:
    if i < 0:
        f = f+i
print([m,f])