import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
dag = [0]*(n+1)
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    dag[y] += 1

def solve():
    build = [0]*(n+1)
    for _ in range(k):
        b, a = map(int,input().split())
        if b == 1: # 건설
            if dag[a] > 0:
                return "Lier!"
            build[a] += 1
            if build[a] != 1: # 이전에 지어진 적 있음
                continue
            for nxt in graph[a]:
                dag[nxt] -= 1
        else:
            if build[a] <= 0: # 지어지지 않은 건물
                return "Lier!"
            build[a] -= 1 # 파괴
            if build[a] != 0:
                continue
            for nxt in graph[a]:
                dag[nxt] += 1
    return "King-God-Emperor"
print(solve())