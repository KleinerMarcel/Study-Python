a = 586
b = len(str(a))
while b !=1:
 a = [int(i) for i in str(a)]
 a = sum(a)
 b = len(str(a))
print(a)