n = int(input())
words = [input().rstrip() for _ in range(n)]
char = dict()
ans = 0
for word in words:
    for i in range(len(word)):
        if word[i] not in char:
            char[word[i]] = 0
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
    ans += int(tmp)
print(ans)