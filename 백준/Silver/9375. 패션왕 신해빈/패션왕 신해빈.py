import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    ans = 1
    cabinet = dict()
    for i in range(n):
        name, frac = map(str,input().rstrip().split())
        if frac not in cabinet:
            cabinet[frac] = [name]
        else:
            cabinet[frac].append(name)
    #print(cabinet)
    for k in cabinet.keys():
        ans *= len(cabinet[k])+1
    print(ans-1)