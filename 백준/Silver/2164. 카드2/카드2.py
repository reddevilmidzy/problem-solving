from collections import deque

dq = deque()
for i in range(1, int(input()) + 1):
    dq.append(i)

# print(dq.popleft())
while len(dq) > 1:
    dq.popleft() # 가장 처음에 있는 것을 뺀다
    dq.append(dq.popleft()) # 가장 처음에 있던 것을 가장 마지막에 추가

print(dq.pop())