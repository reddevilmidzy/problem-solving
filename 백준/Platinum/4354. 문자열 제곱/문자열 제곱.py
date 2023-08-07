import sys
input = sys.stdin.readline

def kmp(s:str, n:int):
    fail = [0]*n
    i = 0
    for j in range(1, n):
        while i > 0 and s[i] != s[j]:
            i = fail[i-1]
        if s[i] == s[j]:
            i += 1
            fail[j] = i
    # print(fail)
    if (n-fail[-1]) * (n//(n - fail[-1])) == n:
        return n//(n - fail[-1])
    return 1

while True:
    s = input().rstrip()
    if s==".":break
    print(kmp(s,len(s)))