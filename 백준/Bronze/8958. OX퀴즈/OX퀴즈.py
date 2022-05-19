import sys
input = sys.stdin.readline
test_case = int(input().rstrip()) # 몇개 오는지 확인
ox = [] # ox 담을거
for i in range(test_case):
  xoxo = input().rstrip()
  ox.append(xoxo)
  long = (len(ox[i]))
  plus = 0
  score = []
  for u in range(long):
    if (ox[i])[u] == "X":
      score.append(0)
      plus = 0
    elif (ox[i])[u] == "O":
      plus += 1
      score.append(plus)
  print(sum(score))