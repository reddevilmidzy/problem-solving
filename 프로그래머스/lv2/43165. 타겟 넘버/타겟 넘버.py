canditate = []

def bt(s,n):
    if len(s) == n:
        global canditate
        canditate.append(s[::])
        return
    elif len(s) > n:
        return

    for x in [1,-1]:
        s.append(x)
        bt(s,n)
        s.pop()


def solution(numbers, target):
    answer = 0
    n = len(numbers)
    bt([], n)
    tmp = []
    for candi in canditate:
        tmp_sum = 0
        for x,y in zip(numbers, candi):
            tmp_sum += x*y
        
        if tmp_sum == target:
            answer += 1
       
    return answer