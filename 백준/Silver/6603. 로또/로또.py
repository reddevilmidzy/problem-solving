import sys
input = sys.stdin.readline

def dfs():
    if len(stk) == 6:
        print(*stk)
        return
    for i in s:
        if i not in stk:
            if len(stk) == 0:
                stk.append(i)
                dfs()
                stk.pop()
            elif stk[-1] < i:
                stk.append(i)
                dfs()
                stk.pop()

while True:
    n = list(map(int, input().rstrip().split()))
    if n[0] == 0:
        break
    k = n[0]
    s = n[1:]
    stk = []
    dfs()
    print('')