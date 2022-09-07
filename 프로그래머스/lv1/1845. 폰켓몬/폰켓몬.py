def solution(nums):
    answer = 0
    no_double = len(set(nums))
    if no_double > len(nums)//2:
        answer = len(nums)//2
    else:
        answer = no_double
    return answer