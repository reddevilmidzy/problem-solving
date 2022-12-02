import sys
from itertools import combinations
input = sys.stdin.readline

def sum_taste(s):
    return sum(s)

def times_taste(s):
    res = 1
    for i in s:
        res *= i
    return res

def formated(string):
    string = str(string)
    string = string[1:-1]
    string = string.replace(","," ")
    string = string.replace("(", "")
    string = string.replace(")", "")
    return list(map(int,string.split()))



n = int(input())
s_taste = []
b_taste = []

for _ in range(n):
    s,b = map(int,input().split())
    s_taste.append(s)
    b_taste.append(b)


res = 1000000000
for i in range(1, n+1):
    s_nums = [num for num in combinations(s_taste, i)]
    b_nums = [num for num in combinations(b_taste, i)]
    for j in range(len(s_nums)):
        s_list = s_nums[j]
        b_list = b_nums[j]
        ans = abs(times_taste(formated(s_list))-sum_taste(formated(b_list)))
        res = min(ans, res)

print(res)