import sys
sys.setrecursionlimit(10**5)

def recursion(cur:int, nxt:int, length:int) -> None:
    global ans
    if length > ans:
        ans = length
    
    if nxt >= n: return
    if s[cur] == s[nxt]:
        recursion(nxt,nxt+1,length+1)
    else:
        recursion(cur,nxt+2,length)

s=input()
n=len(s)
ans = 1
for i in range(n//2):
    recursion(i,i+1,1)
    
print(ans)