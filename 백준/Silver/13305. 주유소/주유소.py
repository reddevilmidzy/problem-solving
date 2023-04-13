n = int(input())
dist = list(map(int,input().split()))
money = list(map(int,input().split()))

ans = 0
won = money[0]

for i in range(n-1):
    ans += dist[i] * won
    if won > money[i+1]:
        won = money[i+1]
print(ans)