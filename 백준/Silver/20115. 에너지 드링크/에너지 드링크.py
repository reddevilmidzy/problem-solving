import sys
input = sys.stdin.readline
n=int(input())
nums= list(map(int,input().split()))
print(sum(nums)/2+max(nums)/2)