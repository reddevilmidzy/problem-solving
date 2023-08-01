import sys
input = sys.stdin.readline

def kmp(n, pattern, m, string):
    pi = [0]*n
    i = 0
    for j in range(1, n):
        while i > 0 and pattern[i] != pattern[j]:
            i = pi[i-1]
        if pattern[i] == pattern[j]:
            i += 1
            pi[j] = i
    
    i = 0
    for j in range(m):
        while i > 0 and string[j] != pattern[i]:
            i = pi[i-1]
        if string[j] == pattern[i]:
            if i == n-1:
                return True
            else:
                i += 1
    return False

t = int(input())
songs = [list(map(int,input().split())) for _ in range(t)]

for i in range(t):
    song = songs[i][1:]
    tmp = []
    for j in range(1, songs[i][0]):
        tmp.append(song[j] - song[j-1])
    songs[i][1:] = tmp[:]

n = int(input())
tmp = list(map(int,input().split()))
db = [tmp[i] - tmp[i-1] for i in range(1, n)]

ans = []

for idx in range(1, t+1):
    if kmp(n-1, db, songs[idx-1][0]-1, songs[idx-1][1:]):
        ans.append(idx)

print(*ans if ans else [-1])