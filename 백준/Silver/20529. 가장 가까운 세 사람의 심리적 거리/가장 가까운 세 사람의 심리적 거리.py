import sys
input = sys.stdin.readline

def diff(a:str, b:str, c:str) -> int:
    res = 0
    for i in range(4):
        res += (a[i]!=b[i])+(b[i]!=c[i])+(c[i]!=a[i])
    return res

def brute(n:int):
    if n > 32: return 0
    cnt = dict()
    for m in mbti:
        if m in cnt and cnt[m] > 2: return 0
        elif m in cnt: cnt[m] += 1
        else: cnt[m] = 1

    res = 8
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                tmp = diff(mbti[i], mbti[j], mbti[k])
                if res > tmp:
                    res = tmp
                    if not res: return 0
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    mbti = list(input().rstrip().split())
    print(brute(n))