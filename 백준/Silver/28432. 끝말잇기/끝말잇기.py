import sys
input = sys.stdin.readline

n = int(input())

words = [input().rstrip() for _ in range(n)]
m = int(input())
candy = [input().rstrip() for _ in range(m)]

use = set(words)

pre = ""
suf = ""

for i in range(n):
    if words[i] == "?":
        if i!=0:
            pre = words[i-1][-1]
        if i!=n-1:
            suf = words[i+1][0]

for can in candy:
    if (pre == "" or pre == can[0]) and (suf == "" or suf == can[-1]) and can not in use:
        print(can)
        break