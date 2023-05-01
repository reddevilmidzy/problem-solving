import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n,k,t,m = map(int,input().split())
    # 각 팀마다 문제 점수 넣기
    scores = [[0]*(k+3) for _ in range(n+1)]
    # scores[k][1:-2] 까지는 문제당 해당 팀에 점수
    # scores[k[0]  제출 횟수
    # scores[k][-2] 마지막 제출 횟수
    # scores[k][-1] # 팀 번호
    order = []
    for i in range(1, n+1):
        scores[i][-1] = i

    for time in range(m):
        i,j,s = map(int,input().split())
        scores[i][j] = max(scores[i][j], s) # 점수 기록
        scores[i][0] += 1 # 제출횟수 기록
        scores[i][-2] = time # 제출시간 기록

    scores = scores[1:]
    scores.sort(key=lambda x: (-sum(x[1:-2]), x[0], x[-2]))

    rank = 1
    for score in scores:
        if score[-1] == t:
            print(rank)
            break
        rank += 1