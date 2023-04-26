from collections import deque
import sys
input = sys.stdin.readline

def solve(words: list[str]) -> str:
    res = words[0]
    for word in words[1:]:
        if res[0] >= word:
            res = word + res
        else:
            res += word
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    words = list(map(str,input().rstrip().split()))
    print(solve(words))