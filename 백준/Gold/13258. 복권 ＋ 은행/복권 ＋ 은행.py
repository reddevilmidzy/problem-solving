import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
j = int(input())
c = int(input())
bank = [nums[0], sum(nums[1:])]

for _ in range(c):
    bank = [bank[0]+j * bank[0]/(sum(bank)),bank[1]+j * (bank[1]/sum(bank))]

print(bank[0])