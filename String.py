name = str(input())
n = name.count('x') + name.count('X')
p = name.count('o') + name.count('O')
if n == p:
    print(True)
else:
    print(False)