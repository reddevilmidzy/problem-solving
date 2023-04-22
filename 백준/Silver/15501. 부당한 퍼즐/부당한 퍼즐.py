from collections import deque
n = int(input())
a = deque(map(int,input().split()))
b = deque(map(int,input().split()))
ans = "bad puzzle"

while b[0] != a[0]:
    b.rotate(1)
if a == b or a == deque(reversed(b)):
    ans = "good puzzle"

while b[-1] != a[0]:
    b.rotate(1)
if a == b or a == deque(reversed(b)):
    ans = "good puzzle"

print(ans)