def solution(numbers):
    n = len(numbers)
    answer = [-1]*n
    stk = []
    for i in range(n-1, -1, -1):
        
        while stk:
            if stk[-1] > numbers[i]:
                answer[i] = stk[-1]
                break
            else:
                stk.pop()
        # if not stk:
        stk.append(numbers[i])
        
    
    return answer