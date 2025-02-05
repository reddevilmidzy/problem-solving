def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if int(i**0.5)**2 == i:
            answer -= i
        else:
            answer += i
        
    return answer