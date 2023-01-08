import sys

input = sys.stdin.readline

n_len = input()
n = set(input().rstrip().split())

m_len = input().rstrip()
m = (input().rstrip().split())

for i in range(int(m_len)):
    if m[i] in n:
        print(1)
    else:
        print(0)