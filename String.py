name = "abba"
print(name.translate({ord(i): None for i in 'euioaEUIOA'}))

