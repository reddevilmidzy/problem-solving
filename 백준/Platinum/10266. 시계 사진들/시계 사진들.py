import sys
input = sys.stdin.readline

def kmp(arr:list[int], pattern:list[int]):
    n = len(pattern)
    m = len(arr)
    pi = [0]*n
    i = 0
    for j in range(1, n):
        while i > 0 and pattern[i] != pattern[j]:
            i = pi[i-1]
        if pattern[i] == pattern[j]:
            i += 1
            pi[j] = i
    i = 0

    for j in range(m):
        while i > 0 and arr[j] != pattern[i]:
            i = pi[i-1]
        if arr[j] == pattern[i]:
            if i == n-1:
                return 2
            else:
                i += 1
    return 0

n = int(input())
k = 360000
a = list(map(int,input().split()))
b = list(map(int,input().split()))
b.sort()

pattern = [0]*k
arr = [0]*k
for i in range(n):
    pattern[a[i]] = 1
    arr[b[i]] = 1
arr = arr[b[0]:b[-1]+1]
pattern = pattern + pattern
print("impossible"[kmp(pattern,arr):])