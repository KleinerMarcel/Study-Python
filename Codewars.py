lst = [[3, 10], [5, 6], [45, 8]]
l = []
for i in lst:
    if i[0]>=7 and i[1] >= 5:
        l.append('Senior')
    else:
        l.append('Open')
print(l)
