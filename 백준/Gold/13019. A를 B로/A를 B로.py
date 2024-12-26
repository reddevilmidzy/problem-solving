from collections import Counter
import sys
input = sys.stdin.readline

def solve():
    if Counter(a) != Counter(b):
        return -1
    
    n = len(a)

    i = n-1
    j = n-1
    cnt = 0
    for i in range(n-1, -1, -1):
        if a[i] != b[j]:
            cnt += 1
        else:
            j -= 1

    return cnt

a = input().rstrip()
b = input().rstrip()

print(solve())
