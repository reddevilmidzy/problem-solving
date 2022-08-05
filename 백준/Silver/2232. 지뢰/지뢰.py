import sys
input = sys.stdin.readline
N = int(input())
prev = int(input())

up, equal = True, False
ans = []

for idx in range(1, N):

    now = int(input())

    if prev == now:

        if equal : ans.append([idx, prev])

        elif up : ans.append([idx, prev])

        up, equal = True, True

    

    elif prev > now:

        equal = False

        if up:

            up = False

            ans.append([idx, prev])

    else:

        up, equal = True, False

        if len(ans) >= 1 and ans[-1][1] == prev and ans[-1][0] == idx:

            ans.pop()

    prev = now

if up:

    ans.append([N, prev])

for a, b in ans:

    print(a)