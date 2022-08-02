import sys
from collections import deque
input=sys.stdin.readline

def bfs(a,b):
    queue=deque()
    queue.append([a,''])
    visited={a:1}
    while queue:
        tob,pro=queue.popleft()
        if tob==b:
            return pro
        if tob == 0:
            S=9999
        else:
            S=tob-1

        if len(str(tob)) == 4:
            L = int(str(tob)[1:]+str(tob)[0])
            R = int(str(tob)[-1]+str(tob)[:-1])
        else:
            L = tob*10
            R = int(str(tob)[-1]+str(0)*(4-len(str(tob)))+str(tob)[:-1])


        move=[(2*tob)%10000, S, L, R]
        way=['D','S','L','R']
        for i in range(4):
            if move[i] not in visited and move[i] < 100000:
                visited[move[i]]=1
                queue.append([move[i], pro+way[i]])

        
for _ in range(int(input())):
    a,b=map(int,input().split())
    print(bfs(a,b))