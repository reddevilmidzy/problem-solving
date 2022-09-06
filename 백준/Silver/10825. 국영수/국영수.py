import sys
input = sys.stdin.readline

n = int(input())
graph= []
for _ in range(n):
    name, kor, eng, math = map(str,input().rstrip().split())
    graph.append([int(kor),int(eng),int(math),name])

graph.sort(key=lambda x:(-x[0],x[1],-x[2],x[3]))

for i in graph:
    print(i[-1])