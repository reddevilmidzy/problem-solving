import sys
input = sys.stdin.readline


def bt(s:int, idx:int):
    global ans
    if s==n//2:
        a,b = 0,0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    a += t[i][j]
                elif not visited[i] and not visited[j]:
                    b += t[i][j]
        ans = min(ans, abs(a-b))
        if not ans:
            print(0)
            exit()
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            bt(s+1,i+1)
            visited[i] = False

n = int(input())
t = [list(map(int,input().split())) for _ in range(n)]
ans = sys.maxsize
visited = [False]*(n+1)
start = [0]
visited[0]=True

bt(1,1)
print(ans)