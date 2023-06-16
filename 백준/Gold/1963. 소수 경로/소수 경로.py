from sys import stdin
from collections import deque
input = stdin.readline

def era():
    n = 10000
    primes = [False, False] + [True]*(n-1)
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i+i, n+1, i):
                primes[j] = False
    return {i:primes[i] for i in range(1000, n+1)}

def bfs(st:int, ed:int) -> int:
    queue = deque()
    queue.append((st, 0))
    visited = set()
    visited.add(st)

    while queue:
        cur, cnt = queue.popleft()
        if cur == ed:
            return cnt
        one = [-i for i in range(1, cur%10+1)] + [i for i in range(9-cur%10, 0, -1)]
        ten = [-i*10 for i in range(1, (cur%100)//10+1)] + [i*10 for i in range(9-(cur%100)//10, 0, -1)]
        hun = [-i*100 for i in range(1, (cur%1000)//100+1)] + [i*100 for i in range(9-(cur%1000)//100, 0, -1)]
        tho = [-i*1000 for i in range(1, (cur%10000)//1000)] + [i*1000 for i in range(9-(cur%10000)//1000, 0, -1)]

        for nxt in one:
            if primes[cur+nxt] and cur+nxt not in visited:
                queue.append((cur+nxt, cnt+1))
                visited.add(cur+nxt)
        for nxt in ten:
            if primes[cur+nxt] and cur+nxt not in visited:
                queue.append((cur+nxt, cnt+1))
                visited.add(cur+nxt)
        for nxt in hun:
            if primes[cur+nxt] and cur+nxt not in visited:
                queue.append((cur+nxt, cnt+1))
                visited.add(cur+nxt)
        for nxt in tho:
            if primes[cur+nxt] and cur+nxt not in visited:
                queue.append((cur+nxt, cnt+1))
                visited.add(cur+nxt)
    return "Impossible"
    
primes = era()
t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    print(bfs(a,b))