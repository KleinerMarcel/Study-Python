a = [1,2,]
a[-1] = a[-1]+1
if a[-1] >= 10:
    a[-2] = a[-2]+1
    a[-1] = a[-1]-10
print(a)