def solution(new_id):
    answer = ''
    res = ''
    cnt = 0
    for i in new_id:        
        if i.isalpha():
            answer += i.lower()
        elif i.isalnum():
            answer += i
        elif i=='_' or i=='-' or i=='.':
            answer += i
        else:
            pass
    print(answer)
    
    for j in answer:
        if j == '.':
            cnt += 1
        else:
            if cnt != 0:
                res += '.'
            res += j
            cnt = 0
    
    
    if res == '':
        res = 'a'
    
    if res[0] == '.':
        # print('바꾸')
        res = res.replace('.','',1)
    
    n = len(res)
        

    
    if n >= 16:
        res = res[:15]
        if res[-1] == '.':
            res = res[:14]
    elif n == 2:
        res += res[-1]
    elif n == 1:
        res = res*3
    
    print(res)
    return res