from sys import stdin
import heapq

n, p = map(int, stdin.readline().split())
stack = [[] for _ in range(7)]
res = 0

for _ in range(n):
    j, f = map(int, stdin.readline().split())

    if not stack[j]:
        heapq.heappush(stack[j], f)
        res += 1

    elif stack[j][-1] < f:
        heapq.heappush(stack[j], f)
        res += 1

    elif stack[j][-1] > f:
        while 1:
            if not stack[j]:
                res += 1
                stack[j].append(f)
                break
            if stack[j][-1] <= f:
                if stack[j][-1] < f:
                    heapq.heappush(stack[j], f)
                    res += 1
                break
            stack[j].pop()
            res += 1

print(res)