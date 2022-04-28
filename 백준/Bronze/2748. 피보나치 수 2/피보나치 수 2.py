import sys
input = sys.stdin.readline

n = int(input())
a = [0,1]
if n == 1 or n ==0:
    print(a[n])
else:

    for i in range(2, n+1):
        a.append(a[i-1] + a[i-2])
    print(a[-1])