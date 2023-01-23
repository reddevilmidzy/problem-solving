import sys
input = sys.stdin.readline

def to_ascii(char):

    if is_upper(char):
        return ord(char) - 65
    
    return ord(char) - 71

def to_alpah(num):
    if num < 26:
        return chr(num + 65)
    return chr(num + 71)
    


def is_upper(char):
    return char.isupper()

INF = int(1e9)
graph = [[INF]*52 for _ in range(52)]
ans = []
n = int(input())
for _ in range(n):
    p,sign,q = map(str,input().rstrip().split())
    graph[to_ascii(p)][to_ascii(q)] = 1

# for k in range(52):
#     graph[k][k] = 0

for x in range(52):
    for i in range(52):
        for j in range(52):
            if graph[i][j] > graph[i][x] + graph[x][j]:
                graph[i][j] = graph[i][x] + graph[x][j]


for i in range(52):
    for j in range(52):
        if graph[i][j] != INF and i!=j:
            ans.append([i,j])
print(len(ans))
for p,q in ans:
    print(to_alpah(p),to_alpah(q),sep=" => ")