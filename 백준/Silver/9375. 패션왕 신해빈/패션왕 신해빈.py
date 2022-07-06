import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    ans = 1
    cabinet = dict()
    for i in range(n):
        name, frac = map(str,input().rstrip().split())
        if frac not in cabinet.keys():
            cabinet[frac] = 1
        else:
            cabinet[frac] += 1
    #print(cabinet)
    for k in cabinet.keys():
        ans *= cabinet[k]+1
    print(ans-1)