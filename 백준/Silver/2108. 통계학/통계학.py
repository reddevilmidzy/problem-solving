import sys

input = sys.stdin.readline
long = int(input().rstrip())
ave = []
ave_ = {}

for i in range(long):
    n = int(input().rstrip())
    ave.append(n)
    if n in ave_:
        ave_[n] += 1
    else:
        ave_[n] = 1

max_val = max(ave_.values())
max_ans = []
for k, j in ave_.items():
    if j == max_val:
        max_ans.append(k)

max_ans.sort()
# print(max_ans, len(max_ans)) # 테스트
if len(max_ans) == 1:
    ans = str(max_ans[0])
    # print(ans, "정답")
else:
    ans = str(max_ans[1])
    # print(ans, "정답")

ave.sort()
print(round(sum(ave)/long)) # 산술 평균
print(ave[(long//2)])
print(ans)
print(max(ave)-min(ave))