from collections import defaultdict
def solution(N, stages):
    answer = []
    player = len(stages)
    now = defaultdict(int)
    for i in stages:
        now[i] += 1
    #print(now)
    for j in range(1,N+1):
        #print(now[j], player)
        if player == 0:
            answer.append((0,j))
        else:
            answer.append((now[j]/player,j))
            player -= now[j]
    answer.sort(key=lambda x:(-x[0],x[1]))
    #print(answer)
    ans = [i[1] for i in answer]
    return ans