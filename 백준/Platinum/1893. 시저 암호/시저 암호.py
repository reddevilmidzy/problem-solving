import sys
input = sys.stdin.readline

def kmp(pattern:list[str]) -> list[int]:
    n = len(pattern)
    pi = [0]*n
    i = 0

    for j in range(1, n):
        while i > 0 and pattern[i] != pattern[j]:
            i = pi[i-1]
        
        if pattern[i] == pattern[j]:
            i += 1
            pi[j] = i

    return pi

def decoded(txt:list[str], order:list[str], pattern:list[str]) -> list[int]:
    n = len(txt)
    m = len(pattern)
    len_order = len(order)

    idx_dict = {order[i]:i for i in range(len(order))}
    res = []

    for idx in range(len_order):
        ss = [order[(idx_dict[k]+idx)%len_order] for k in pattern]
        i = 0
        j = 0
        cnt = 0
        pi = kmp(ss)

        while (n-i) >= (m-j):
            if ss[j] == txt[i]:
                i += 1
                j += 1
            
            if j == m:
                cnt += 1
                j = pi[j-1]
            
            elif i < n and ss[j] != txt[i]:
                if j != 0:
                    j = pi[j-1]
                else:
                    i += 1
        if cnt == 1:
            res.append(idx)

    res.sort()
    return res

t = int(input())
for _ in range(t):
    a = list(input().rstrip())
    w = list(input().rstrip())
    s = list(input().rstrip())

    res = decoded(s,a,w)

    if not res:
        print("no solution")
    elif len(res) == 1:
        print("unique:",*res)
    else:
        print("ambiguous:",*res)