import sys
#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
s = input().rstrip()

stk = []

pattern = "skeep"
res = 0

def same(a: str):
    if len(a) < 5:
        return False
    if a[0] != "s":
        return False
    for i in range(1, 5):
        if a[i] != pattern[i] and a[i] != "#":
            return False
    return True

for i in s:
    stk.append(i)
    while len(stk) >= 5 and same("".join(stk[-5:])):
        stk[-5:] = ['#']
        res += 1

print(res)