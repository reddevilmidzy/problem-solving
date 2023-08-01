def kmp(n, pattern):
    fail = [0]*n
    i = 0
    for j in range(1, n):
        while i > 0 and pattern[i] != pattern[j]:
            i = fail[i-1]
        
        if pattern[i] == pattern[j]:
            i += 1
            fail[j] = i
    return n - fail[n-1]

print(kmp(int(input()), input()))