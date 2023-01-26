import sys
si = sys.stdin.readline
n,m = map(int, si().split())
ans = sorted(list(set([si().rstrip() for i in range(n)]) & set([si().rstrip() for i in range(m)])))
print(len(ans),*ans, sep='\n')