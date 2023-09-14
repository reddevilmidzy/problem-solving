import sys
input = sys.stdin.readline

n = int(input())
problem = []
time = dict()
time[(0,0)] = -1
time[(0,1)] = 0

for i in range(1, n+1):
    query = list(map(str,input().rstrip().split()))
    if query[0] == 'a':
        time[(i, 0)] = int(int(query[1]))
        time[(i,1)] = i-1

    elif query[0] == 't':
        k = int(query[1])
        time[(i,0)] = time[(k-1, 0)]
        time[(i,1)] = time[(k-1, 1)]
    elif query[0] == "s":
        time[(i, 0)] = time[(time[(i-1,1)], 0)]
        time[(i, 1)] = time[(time[(i-1,1)], 1)]

    print(time[(i,0)])