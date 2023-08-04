def kmp(pattern):
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
word, k = input().split()
pi = kmp(word)
n = len(word)
k = int(k)
print(n + (n-pi[-1])*(k-1))