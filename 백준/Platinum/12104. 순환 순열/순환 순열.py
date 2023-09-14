def kmp(s:str, pattern:str) -> int:
    n = len(pattern)
    m = len(s)
    pi = [0]*n
    i = 0

    for j in range(1, n):
        while i > 0 and pattern[i] != pattern[j]:
            i = pi[i-1]
        
        if pattern[i] == pattern[j]:
            i += 1
            pi[j] = i
    
    res = 0
    i = 0
    for j in range(m):
        while i > 0 and s[j] != pattern[i]:
            i = pi[i-1]
        
        if s[j] == pattern[i]:
            if i == n-1:
                res += 1
                i = pi[i]
            else:
                i += 1

    return res

a = input()
b = input()
a = a+a[:-1]

print(kmp(a, b))