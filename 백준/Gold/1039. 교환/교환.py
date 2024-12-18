from collections import deque
import sys
input = sys.stdin.readline

def bfs(num: str):
    queue = deque()
    queue.append((num, 0))
    visited = set()
    visited.add((num, 0))
    res = -1
    while queue:
        cur,cnt = queue.popleft()
        if cnt == k:
            res = max(res, int(cur))
            continue
        
        tmp = list(cur)
        for i in range(len(cur)):
            for j in range(i+1, len(cur)):
                if i==0 and tmp[j] == '0': 
                    continue
                tmp[i],tmp[j] = tmp[j],tmp[i]
                new = ''.join(tmp)
                if (new, cnt+1) not in visited:
                    visited.add((new, cnt+1))
                    queue.append((new, cnt+1))
                
                tmp[i],tmp[j] = tmp[j],tmp[i]
    
    return res

n,k = map(int,input().split())
# num = list(str(n))
num = str(n)
print(bfs(num))
