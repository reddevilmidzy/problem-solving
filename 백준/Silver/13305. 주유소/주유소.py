n = int(input())
road = list(map(int, input().split()))
coin = list(map(int, input().split()))
result = 0
cheap = coin[0]
for i in range(n-1):
    result += road[i]*cheap
    if cheap <= coin[i+1]:
        pass
    else:
        cheap = coin[i+1]
print(result)