def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
print(series_sum (1) )

n = 2
s = 0.0
n = range(0,n)
for i in n:
    s += 1/(1+3*float(i))
print(s)

def series_sum(n):
    s = 0.0
    n = range(0,n)
    for i in n:
        s += 1/(1+3*float(i))
    return '{:.2f}'.format(s)