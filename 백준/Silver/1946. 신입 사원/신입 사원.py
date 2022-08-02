import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    score=sorted([list(map(int,input().split())) for i in range(n)])
    ans=1
    now=score[0][1]
    for j in range(1, n):
        if now>score[j][1]:
            ans+=1
            now=score[j][1]
    print(ans)