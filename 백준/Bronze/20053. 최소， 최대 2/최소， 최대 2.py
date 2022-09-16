import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    print(min(nums), max(nums))