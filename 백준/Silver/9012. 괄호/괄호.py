import sys
input = sys.stdin.readline
for i in range(int(input().rstrip())):
    stk = []
    ans = "YES"
    vps = list(input().rstrip())
    for j in vps:
        try:
            if j == "(":
                stk.append(j)
            else:
                stk.pop()
        except:
            ans = "NO"
            break
    print(ans) if len(stk) == 0 else print("NO")