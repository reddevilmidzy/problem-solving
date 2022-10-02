from collections import deque
def solution(queue1, queue2):
    answer = -1
    res = 0
    n= len(queue1)+len(queue2)
    left = sum(queue1)
    right = sum(queue2)
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    for i in range(n+2):
        #print(queue1, queue2, left, right)
        if left<right:
            tmp = queue2.popleft()
            queue1.append(tmp)
            right -= tmp
            left += tmp
            res += 1
        elif left>right:
            tmp = queue1.popleft()
            queue2.append(tmp)
            left -= tmp
            right += tmp
            res += 1
        if left==right:
            return res
    return answer