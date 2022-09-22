def solution(survey, choices):
    mbti = {'R':0, 'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    answer = ''
    tmp = ['R','T','C','F','J','M','A','N']
    n = len(survey)
    for i in range(n):
        a,b = survey[i][0],survey[i][1]
        # print('a',a,'b',b)
        if choices[i] < 4:
            # 자리 찾아서 값을 더해줘야 함 abs(choices[i]-4)
            mbti[a] += abs(choices[i]-4)
        elif choices[i]==4:
            pass
        else:
            # 뒤에거 더해줌
            mbti[b] += abs(choices[i]-4)
    
    for i in range(0,7,2):
        if mbti[tmp[i]] >= mbti[tmp[i+1]]:
            answer += tmp[i]
        else:
            answer += tmp[i+1]
            
    return answer