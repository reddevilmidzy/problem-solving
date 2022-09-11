import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(root, check,visited):
    global x_ans
    global y_ans
    if check == 0:
        #print('x',root)
        x_ans.append(root)
    else:
        if root in x_ans:
            print(root)
            return
        #print('y',root)
        y_ans.append(root)
    for i in re_tree[root]:
        if not visited[i]:
            visited[i] = True
            dfs(i,check, visited)
        

for _ in range(int(input())):
    n = int(input())
    # tree = [[] for _ in range(n+1)]
    x_visited = [False]*(n+1)
    y_visited = [False]*(n+1)
    
    x_ans = []
    y_ans = []
    re_tree = [[] for _ in range(n+1)]
    for __ in range(n-1):
        a,b = map(int,input().split())
        # tree[a].append(b)
        re_tree[b].append(a)
    
    x,y = map(int,input().split())
    x_visited[x] = True
    dfs(x,0,x_visited)
    y_visited[y] = True
    dfs(y,1,y_visited)
    #print(x_ans, y_ans)