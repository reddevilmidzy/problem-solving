import sys
input = sys.stdin.readline
five = [5**i for i in range(1, 13)]

for i in range(int(input().rstrip())):
    n = int(input().rstrip())
    cnt = 0
    for f in five:
        cnt += n//f
    print(cnt)