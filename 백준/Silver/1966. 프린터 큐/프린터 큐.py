import sys
from collections import deque
input = sys.stdin.readline

for i in range(int(input().rstrip())):
    queue = deque()
    n,m = map(int, input().rstrip().split())
    imp = list(map(int, input().rstrip().split()))
    for j in range(n):
        queue.append((imp[j], j))
    cnt = 0
    start = True
    while start:
        max_imp = max(imp)

        for j in range(len(queue)):
            paper = queue.popleft()
            if paper[0] == max_imp:
                cnt += 1
                if paper[1] == m:
                    print(cnt)
                    start =False
                    break
                else:
                    imp.remove(max_imp)
                    break
            else:
                queue.append(paper)