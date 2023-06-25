from math import ceil
import sys
input = sys.stdin.readline

def solve(word:chr):
    s = word[:ceil(len(word)/3)]
    rs = s[::-1]
    return s+rs+s == word or s+rs[1:]+s == word or s+rs+s[1:] == word or s+rs[1:]+s[1:] == word
t = int(input())
for _ in range(t):
    word = input().rstrip()
    print(int(solve(word)))