import sys
input = sys.stdin.readline
memo = dict()
n, m = map(int, input().rstrip().split())


for i in range(n):
    site, password = map(str, input().rstrip().split())
    memo[site] = password

for u in range(m):
    print(memo[input().rstrip()])