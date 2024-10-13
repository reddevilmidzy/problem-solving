from bisect import bisect_left, bisect_right
import sys
#sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n = int(input())

def solve():
    a,b,c,d, = [], [], [], []

    for _ in range(n):
        tmp = list(map(int,input().split()))
        a.append(tmp[0])
        b.append(tmp[1])
        c.append(tmp[2])
        d.append(tmp[3])

    a1 = []
    b1 = []
    for i in range(n):
        for j in range(n):
            a1.append(a[i] + b[j])
            b1.append(c[i] + d[j])

    a1.sort()
    b1.sort()

    res = 0
    idx = 0

    m = n*n
    while idx < m:
        left = bisect_left(b1, -a1[idx])

        if left < m and -a1[idx] == b1[left]:
            right = bisect_right(b1, -a1[idx])
            res += (right - left)
        
        idx += 1

    return res
print(solve())