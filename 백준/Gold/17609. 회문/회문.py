import sys
input = sys.stdin.readline

def is_palindrome(word: str) -> bool:
    return word == word[::-1]

def is_similarity_palindrome(word: str) -> bool:
    n = len(word)
    left, right = 0, n-1
    delete = False
    while left <= right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        elif not delete:
            tmp = word[left:right+1]
            if is_palindrome(tmp[1:]):
                left += 2
                right -= 1
            elif is_palindrome(tmp[:-1]):
                left += 1
                right -= 2
            else:
                return False                
            delete = True
        else:
            return False
    return True

t = int(input())
for _ in range(t):
    word = input().rstrip()
    if is_palindrome(word):
        print(0)
    elif is_similarity_palindrome(word):
        print(1)
    else:
        print(2)