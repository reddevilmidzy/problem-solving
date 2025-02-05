def solution(left, right):
    return sum([i * (1 + -2 * (int(i**0.5)**2 == i)) for i in range(left, right + 1)])
