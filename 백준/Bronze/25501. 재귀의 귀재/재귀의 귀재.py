import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().rstrip()
    if s==s[::-1]:
        print(1, (len(s)+2)//2)
    else:
        idx = 0
        while idx < len(s):
            if s[idx] != s[-idx-1]:
                break
            idx += 1
        print(0, idx+1)