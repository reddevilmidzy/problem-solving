import sys
input = sys.stdin.readline

while True:
    a,b= map(int,input().rstrip().split())
    if a + b == 0:
        break
    print('Yes') if a > b else print('No')