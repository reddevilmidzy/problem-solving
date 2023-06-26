from collections import defaultdict
n = int(input())
words = [input().rstrip() for _ in range(n)]
char = defaultdict(int)

for word in words:
    for i in range(len(word)):
        char[word[i]] += 10 ** (len(word) - i - 1)

rep = dict()
num = 9

for key in sorted(char.keys(), key=lambda x:-char[x[0]]):
    rep[key] = num
    num -= 1

for i in range(n):
    tmp = ""
    for j in range(len(words[i])):
        tmp += str(rep[words[i][j]])
    words[i] = int(tmp)

print(sum(words))