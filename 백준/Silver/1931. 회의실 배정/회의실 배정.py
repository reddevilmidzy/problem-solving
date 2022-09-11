import sys
input = sys.stdin.readline

n = int(input())
meet = []

for i in range(n):
    a,b= map(int,input().split())
    meet.append([a,b])

meet.sort(key=lambda x: (x[1],x[0]))

ans = 0
end = 0

for i in range(len(meet)):
    if end <= meet[i][0]:
        end = meet[i][1]
        ans += 1
        
print(ans)