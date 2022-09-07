import sys
input = sys.stdin.readline
nums = sorted([int(input()) for _ in range(int(input()))])
print(*nums, sep='\n')