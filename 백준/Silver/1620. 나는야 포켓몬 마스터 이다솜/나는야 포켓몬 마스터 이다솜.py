import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
poketmon = dict()
for i in range(1, n+1):
    name = input().rstrip()
    poketmon[name] = i
    poketmon[str(i)] = name

for j in range(m):
    guess = input().rstrip()
    print(poketmon[guess])