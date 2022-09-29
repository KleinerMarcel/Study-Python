def large(x):
    v = []
    while len(x) != 0:
        for i in x:
            if len(i.lower()) == 4:
                v.append(i)
        return v


print(large(['oSH', 'bfqy', 'fAxqbVpRW', 'qlIeyEluFtqFci', 'gaNJ', 'uXgNPFGKhVPOygUNFzw', 'xfdt']))
