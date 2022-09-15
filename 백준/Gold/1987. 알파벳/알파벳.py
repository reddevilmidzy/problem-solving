import sys
input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]
r,c = map(int,input().split())
graph = [list(map(str,input().rstrip())) for _ in range(r)]
ans = 1
tmp = [False]*(26)
# tmp = {'A': 0,'B':0,'C':0,'D': 0,'E':0,'F':0,'G':0,'H':0,'I':0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P':0,'Q': 0, 'R': 0, 'S': 0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
def dfs(a,b,d,dic):
    # print('ans',ans)
    global ans
    for i in range(4):
        nx = a+dx[i]
        ny = b+dy[i]
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        alpha= ord(graph[nx][ny])-65
        if not dic[alpha]:
            ans = max(ans, d+1)
            # ans.append(d+1)
            # print('ans',ans)
            dic[alpha] = True
            dfs(nx,ny,d+1,dic)
            dic[alpha] = False
    #print('ans',ans)
# 제발
tmp[ord(graph[0][0])-65]= True
dfs(0,0,1,tmp)
print(ans)
#print(max(ans))
# print(dfs(0,0,1,tmp,ans))