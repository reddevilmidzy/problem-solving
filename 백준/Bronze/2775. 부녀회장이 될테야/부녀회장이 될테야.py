import sys
input = sys.stdin.readline

for t in range(int(input())):
    k= int(input().rstrip())
    n = int(input().rstrip())
    arr = [num for num in range(1, n+1)] # 0층에 사는 친구
    for i in range(k):
        new = []
        for j in range(n):
            new.append(sum(arr[:j+1]))
        arr= new.copy()
    print(arr[-1])