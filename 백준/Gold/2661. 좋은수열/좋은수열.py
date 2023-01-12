def bt(s):
    if len(s) == n:
        print(*s,sep='')
        exit(0)
    elif len(s) > n:
        return 
    for i in nums:
        if check(s, i):
            s.append(i)
            bt(s)
            s.pop()

def check(word,i):
    word.append(i)
    for i in range(2, len(word)+1, 2):
        for j in range(0, len(word)-i+1):
            if word[j:i+j-i//2] == word[j+i//2:i+j]:
                word.pop()
                return False
    word.pop()
    return True

n = int(input())
nums = [1,2,3]
bt([])