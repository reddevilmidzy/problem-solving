def solution(s):
    res = []
    n = len(s)
    sdt = {"S": 1, "D": 2, "T": 3}
    score = 0
    i = 0
    while i < n:
        if s[i].isalnum():
            score = ''
            while i < n and s[i].isnumeric():
                score += s[i]
                i += 1
            score = int(score)
            res.append(score**sdt[s[i]])
        elif s[i] == "*":
            for j in range(len(res)-1, max(len(res)-3, -1), -1):
                res[j] *= 2
        elif s[i] == "#":
            res[-1] *= -1
        i += 1
            
    return sum(res)
