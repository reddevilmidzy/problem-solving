from itertools import combinations
from collections import Counter
import sys
input = sys.stdin.readline

def diff(a:str, b:str, c:str) -> int:
    res = 0
    for i in range(4):
        res += (a[i]!=b[i])+(b[i]!=c[i])+(c[i]!=a[i])
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    mbti = list(input().rstrip().split())
    ans = 8
    cnt = Counter(mbti)

    if cnt.most_common(1)[0][1] >= 3:
        print(0)
        continue
    for a,b,c in combinations(mbti, 3):
        if ans > diff(a,b,c):
            ans = diff(a,b,c)
    print(ans)