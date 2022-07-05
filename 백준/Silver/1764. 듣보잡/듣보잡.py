import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heard = set([input().rstrip() for i in range(n)])
see = set([input().rstrip() for i in range(m)])

ans = list(heard & see)
ans.sort()
print(len(ans))
for i in ans:
    print(i)