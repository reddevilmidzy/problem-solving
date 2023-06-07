from collections import Counter
import sys
input = sys.stdin.readline

def diff(a:str, b:str, c:str) -> int:
    res = 0
    for i in range(4):
        res += (a[i]!=b[i])+(b[i]!=c[i])+(c[i]!=a[i])
    return res

def brute(n:int):
    if n > 32: return 0
    cnt = Counter(mbti)
    if cnt.most_common(1)[0][1] > 2: return 0    
    res = 8
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                tmp = diff(mbti[i], mbti[j], mbti[k])
                if res > tmp:
                    res = tmp
                    if not res: return res
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    mbti = list(input().rstrip().split())
    print(brute(n))