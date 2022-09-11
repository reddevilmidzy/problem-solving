def solution(arr):
    answer = [arr[0]]
    pre = arr[0]
    for i in range(1,len(arr)):
        if arr[i] != pre:
            answer.append(arr[i])
            pre = arr[i]
        else:
            pass
        
            
    return answer