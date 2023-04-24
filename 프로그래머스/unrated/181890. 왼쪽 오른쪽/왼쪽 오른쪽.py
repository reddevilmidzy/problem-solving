def solution(str_list):
    answer = []
    for idx,char in enumerate(str_list):
        if char == "l":
            answer.extend(str_list[:idx])
            break
        elif char == "r":
            answer.extend(str_list[idx+1:])
            break
        
    return answer