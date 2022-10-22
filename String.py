from collections import Counter
word = "hello"
word = word.lower()
counter = Counter(word)
print(counter, ''.join(('(' if counter[c] == 1 else ')') for c in word))