from collections import Counter, defaultdict
word = defaultdict(int)
word.update(Counter(input()))
for i in range(97, 123):
    print(word[chr(i)], end=' ')
