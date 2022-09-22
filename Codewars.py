lst = [(3, 10), (5, 6), (45, 4)]
lst = [i[0]+i[1] for i in lst]
lst2 = []
for i in lst:
    if i >=16:
        lst2.append('Senior')
    else:
        lst2.append('Open')
print(lst2)
