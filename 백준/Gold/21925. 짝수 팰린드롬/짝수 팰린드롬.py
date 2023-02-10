from collections import Counter, defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
# n,nums = 10,[1,1,5,6,7,7,6,5,5,5]
# nums = [8,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8]
# n = len(nums)
# n,nums = 6,[1,1,1,1,1,1]
# n,nums = 6,[1,2,3,3,2,2]
pair = defaultdict(bool)
cnt_num = Counter(nums)

dp = [[0]*(n) for _ in range(n)]

for cnt in cnt_num.values():
    if cnt%2:
        print(-1)
        exit()

for i in range(n):
    for start in range(n-i):
        end = start + i
        if start==end:
            dp[start][end]=1
        elif nums[start] == nums[end]:
            if start+1==end:
                dp[start][end]=1
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1

# for i in range(n):
#     for j in range(n):
#         print(dp[i][j], end=' ')
#     print()

queue = deque()
for i in range(n):
    for j in range(i+1,n,2):
        if dp[i][j]:
            queue.append([i,j])

# print(queue)

# print("시작")
ans = 0
ed_idx = -1
# st_idx = queue[0][0]
# print(st_idx, "stidx")

# if st_idx: # 시작점이 팰린드롬이 아님
#     print(-1)
#     exit()

order_arr = []
while queue:
    st, ed = queue.popleft()
    if st > ed_idx:
        order_arr.append([st, ed])
        # print(st, ed, "들어옴")
        ans += 1
        ed_idx = ed
        
# print(ans)
# print(order_arr)
collect_st = 0
for st, ed in order_arr:
    # print(collect_st, "cst")
    if st == collect_st:
        collect_st = ed + 1
    else:
        print(-1)
        break
else:
    # print(collect_st)
    print(ans if collect_st == n else -1)