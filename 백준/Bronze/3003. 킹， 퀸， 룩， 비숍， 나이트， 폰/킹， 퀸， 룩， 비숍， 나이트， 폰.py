white = list(map(int,input().split()))
mal = [1,1,2,2,2,8]
for i in range(6):
    print(mal[i] - white[i],end=' ')